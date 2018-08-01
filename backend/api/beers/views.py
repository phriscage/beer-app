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

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../../')

from lib.utils import http_status_response # noqa
from lib.wrapper import post_beer_details, get_beer_details, get_beer_reviews # noqa

logger = logging.getLogger(__name__)
beers = Blueprint('beers', __name__)

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
