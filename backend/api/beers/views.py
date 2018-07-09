# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position
"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
import os
import sys
# from datetime import datetime
from http import HTTPStatus
import logging
# from urllib.parse import urlparse, unquote
from flask import Blueprint, jsonify, request, abort
import simplejson as json
import requests

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../../')

from lib.utils import http_status_response # noqa

logger = logging.getLogger(__name__)
beers = Blueprint('beers', __name__)

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

def post_beer_details(headers, body):
    """ post the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    try:
        res = requests.post(url, headers=headers, json=body, timeout=3.0)
    except:
        res = None
    if res.status_code in (201, 400):
        return res.status_code, res.json()
    else:
        logger.debug(res.status_code)
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, beer details are currently unavailable.'}

def get_beer_details(beer_id, headers, params=None):
    """ get the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    if beer_id:
        url = beer_details['name'] + "/" + beer_details['endpoint'] + "/" + str(beer_id)
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        logger.debug(res)
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, beer details are currently unavailable.'}

def delete_beer_details(beer_id, headers, params=None):
    """ delete the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint'] + "/" + str(beer_id)
    try:
        res = requests.delete(url, headers=headers, params=params, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        logger.debug(res)
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, beer details are currently unavailable.'}

def get_beer_reviews(beer_id, headers, params=None):
    """ get the beer reviews from the service """
    url = beer_reviews['name'] + "/beer" + "/" + str(beer_id) + "/" + beer_reviews['endpoint']
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        logger.debug(res)
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, beer reviews are currently unavailable.'}


@beers.route('', methods=['GET', 'POST'])
def index():
    """
    """
    headers = {}
    if request.method == 'POST':
        # headers = {'content-type': 'application/json'}
        status, details = post_beer_details(headers, request.json)
    else:
        status, details = get_beer_details(None, headers, request.query_string)
    return jsonify(details), status

@beers.route('/<string:beer_id>', methods=['GET', 'DELETE'])
def get_or_delete_beer_by_beer_id(beer_id):
    """
    """
    headers = {}
    if request.method == 'DELETE':
        status, details = delete_beer_details(beer_id, headers, request.query_string)
    else:
        status, details = get_beer_details(beer_id, headers, request.query_string)
    return jsonify(details), status

@beers.route('/<string:beer_id>/reviews', methods=['GET'])
def get_beer_reviews_by_beer_id(beer_id):
    """
    """
    headers = {}
    status, reviews = get_beer_reviews(beer_id, headers, request.query_string)
    return jsonify(reviews), status
