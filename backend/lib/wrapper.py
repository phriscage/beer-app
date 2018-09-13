# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position
"""
    wrapper file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
from __future__ import print_function

import os
import sys
# from datetime import datetime
import logging
# from urllib.parse import urlparse, unquote
from http.client import HTTPConnection
from http import HTTPStatus
import requests
import simplejson as json

import grpc

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../')

from google.protobuf.json_format import MessageToJson, Parse
import protos.beerlikes.beer_likes_pb2 as bl_pb2
import protos.beerlikes.beer_likes_pb2_grpc as bl_pb2_grpc

HTTPConnection.debuglevel = 1
logger = logging.getLogger(__name__)

beer_details = {
    "name" : "http://details-api:8080",
    "endpoint" : "details",
    "children" : []
}

beer_reviews = {
    "name" : "http://reviews-api:8080",
    "endpoint" : "reviews",
    "children" : []
}

beer_likes = {
    "name" : "likes-api:10000"
}


def post_beer_details(headers, body):
    """ post the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    try:
        res = requests.post(url, headers=headers, json=body, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = str(error)
        return 500, {'message': 'Sorry, [%s] is currently unavailable.' % url, 'error': res}
    if res.status_code in (201, 400):
        return res.status_code, res.json()
    data = {
      'request': {
        'url': url,
        'headers': headers,
        'params': params
      },
      'response': {
        'headers': res.headers,
        'status_code': res.status_code
      }
    }
    logger.debug(data)
    logger.debug(res.text)
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'message': 'Sorry, [%s] is currently unavailable.' % url}

def get_beer_details(beer_id, headers, params=None):
    """ get the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    if beer_id:
        url = beer_details['name'] + "/" + beer_details['endpoint'] + "/" + str(beer_id)
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = str(error)
        return 500, {'message': 'Sorry, [%s] is currently unavailable.' % url, 'error': res}
    if res and res.status_code == 200:
        data = res.json()
        if params.get('likes'):
            beer_data = data.get('data', [])
            if type(beer_data) == dict:
                beer_data = [beer_data]
            data = []
            for beer in beer_data:
                status, likes = get_beer_likes(beer.get('id'), headers, None)
                #if status and status == 200:
                    #beer.update({'likes': likes.get('total_count')})
                beer.update({'likes': likes.get('data', [])})
                beer.update({'likes_total': likes.get('total_count', 0)})
                data.append(beer)
        return 200, data
    data = {
      'request': {
        'url': url,
        'headers': headers,
        'params': params
      },
      'response': {
        'headers': res.headers,
        'status_code': res.status_code
      }
    }
    logger.debug(data)
    logger.debug(res.text)
    return status, {'message': 'Sorry, [%s] is currently unavailable.' % url}

def get_beer_reviews(beer_id, headers, params=None):
    """ get the beer reviews from the service """
    url = beer_reviews['name'] + "/beer" + "/" + str(beer_id) + "/" + beer_reviews['endpoint']
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = str(error)
        return 500, {'message': 'Sorry, [%s] is currently unavailable.' % url, 'error': res}
    if res and res.status_code == 200:
        return 200, res.json()
    data = {
      'request': {
        'url': url,
        'headers': headers,
        'params': params
      },
      'response': {
        'headers': res.headers,
        'status_code': res.status_code
      }
    }
    logger.debug(data)
    logger.debug(res.text)
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'message': 'Sorry, [%s] is currently unavailable.' % url}

def list_likes(query, stub, metadata):
    """ get the likes_summary object in json format """
    req = bl_pb2.LikesQuery(ref_type=bl_pb2.RefType(**query))
    res = stub.ListLikes(req, metadata=metadata)
    like_summary = bl_pb2.LikesSummary()
    for item in res:
        ## There is an error with protobuf that cannot compare the classes
        ## https://github.com/protocolbuffers/protobuf/issues/4928. For now we have to
        ## rebuild the Message from JSON
        # like_summary.likes.extend([item])
        like_summary.likes.extend([Parse(MessageToJson(item), bl_pb2.Like())])
        if item.liked:
            like_summary.total += 1
        else:
            like_summary.total -= 1
    #logger.debug("LikeSummary %s", MessageToJson(like_summary))
    data = json.loads(MessageToJson(like_summary))
    if not data:
        return {
            'code': HTTPStatus.NOT_FOUND.value,
			'status': HTTPStatus.NOT_FOUND.phrase,
            'description': HTTPStatus.NOT_FOUND.description
        }
    return {
      'code': HTTPStatus.OK.value,
      'data': data.get('likes', []),
      'total_count': data.get('total', None),
      'status': HTTPStatus.OK.phrase,
      'description': HTTPStatus.OK.description
    }


def get_beer_likes(beer_id, headers, params=None):
    """ get the beer likes from the service """
    conn = beer_likes['name']
    query = {
        'id': str(beer_id),
        'name': 'beer'
    }
    metadata = []
    if headers.get('x-api-key', None):
        metadata.append(('x-api-key', headers.get('x-api-key')))
    if headers.get('authorization', None):
        metadata.append(('authorization', headers.get('authorization')))
    try:
        with grpc.insecure_channel(conn) as channel:
            stub = bl_pb2_grpc.BeerLikesStub(channel)
            res = list_likes(query, stub, metadata)
    except Exception as error:
        logger.warning(error.debug_error_string())
        res = str(error.code())
        return 500, {'message': 'Sorry, [%s] is currently unavailable.' % conn, 'error': res}
    #if res and res.status_code == 200:
    if res and res.get('code', None) == 200:
        return 200, res
    status = res.get('code', None) if res is not None and res.get('code', None) else 500
    return status, {'message': 'Sorry, [%s] is currently unavailable.' % conn}
