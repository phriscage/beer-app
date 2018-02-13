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


@beers.route('', methods=['GET'])
def get_beers():
    """
    """
    headers = {}
    status, details = get_beer_details(None, headers, request.query_string)
    return jsonify(details), status

@beers.route('/<int:beer_id>', methods=['GET'])
def get_by_beer_id(beer_id):
    """
    """
    headers = {}
    status, details = get_beer_details(beer_id, headers, request.query_string)
    return jsonify(details), status
