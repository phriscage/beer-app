# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position
"""
    wrapper file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
import os
import sys
# from datetime import datetime
import logging
# from urllib.parse import urlparse, unquote
import requests

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../')

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

def post_beer_details(headers, body):
    """ post the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    try:
        res = requests.post(url, headers=headers, json=body, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = None
    if res.status_code in (201, 400):
        return res.status_code, res.json()
    logger.debug(res)
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'error': 'Sorry, beer details are currently unavailable.'}

def get_beer_details(beer_id, headers, params=None):
    """ get the beer details from the service """
    url = beer_details['name'] + "/" + beer_details['endpoint']
    if beer_id:
        url = beer_details['name'] + "/" + beer_details['endpoint'] + "/" + str(beer_id)
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    logger.debug(res)
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'error': 'Sorry, beer details are currently unavailable.'}

def get_beer_reviews(beer_id, headers, params=None):
    """ get the beer reviews from the service """
    url = beer_reviews['name'] + "/beer" + "/" + str(beer_id) + "/" + beer_reviews['endpoint']
    try:
        res = requests.get(url, headers=headers, params=params, timeout=3.0)
    except Exception as error:
        logger.warning(error)
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    logger.debug(res)
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'error': 'Sorry, beer reviews are currently unavailable.'}
