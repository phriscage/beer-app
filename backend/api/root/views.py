# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position
"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
import os
import sys
# from datetime import datetime
from http import HTTPStatus
from random import randint
import logging
# from urllib.parse import urlparse, unquote
from flask import Blueprint, jsonify, request, abort
from flask import current_app as app
from flask_cors import cross_origin
import requests

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../../')

from lib.utils import http_status_response # noqak

logger = logging.getLogger(__name__)
root = Blueprint('root', __name__, static_folder='../../static')


@root.route('/openapi_spec', methods=['GET'])
@root.route('/openapi_spec<string:extension>', methods=['GET'])
def get_openapi_spec(extension=None):
    """ return the yaml openapi_spec in JSON or YAML """
    file_name = 'openapi_spec.json'
    if request.args.get('version', None) == 'v2':
      file_name = 'openapi_spec.v2.json'
    if extension == '.yaml':
       file_name = 'openapi_spec.yaml'
       if request.args.get('version', None) == 'v2':
            file_name = 'openapi_spec.v2.yaml'
    return root.send_static_file(file_name)

@root.route('/random', methods=['GET'])
@cross_origin()
def random_number():
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
        'randomNumber': randint(1, 100)
    }
    return jsonify(data=data, **http_status_response('OK')
                  ), HTTPStatus.OK.value
