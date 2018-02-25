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

from lib.utils import http_status_response, get_fqdn, get_ip_address # noqa

logger = logging.getLogger(__name__)
oauth = Blueprint('oauth', __name__)


@oauth.route('/token/refresh', methods=['GET', 'POST'])
@oauth.route('/token', methods=['GET', 'POST'])
def return_token():
    """
    **Example request:**

    .. sourcecode:: http

    GET HTTP/1.1
    Accept: */*

    **Example response:**

    .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    :statuscode 200: Ok
    :statuscode 500: server error
    """
    ## return the access token (id_token or access) from the provider
    headers = {
        'Access-Control-Expose-Headers': 'Authorization',
        'Authorization': request.headers.get('Authorization', None)
    }
    data = {
        'access_token': request.headers.get('Authorization', None),
        'id_token': request.headers.get('X-Provider-id_token', None),
    }
    return jsonify(message="Success", **data, **http_status_response('OK')
                  ), HTTPStatus.OK.value, headers
    # return abort(400)

@oauth.route('/user', methods=['GET', 'POST'])
def get_user():
    """
    **Example request:**

    .. sourcecode:: http

    GET HTTP/1.1
    Accept: */*

    **Example response:**

    .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    :statuscode 200: Ok
    :statuscode 500: server error
    """
    data = {
      'id': 1,
      'username': 'admin',
      'email': 'abc@123.com',
      'role': 'user',
      'created_at': "2017-01-10 17:18:22",
      'updated_at': "2017-01-10 17:18:22"
    }
    return jsonify(message="Success", data=data, **http_status_response('OK')
                  ), HTTPStatus.OK.value
