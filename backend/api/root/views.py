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
root = Blueprint('root', __name__)


@root.route('/', defaults={'path': ''})
@root.route('/<path:path>')
def catch_all(path):
    ## This reroutes to the NPM dev instance
    if app.debug:
        return requests.get('http://docker.for.mac.host.internal:8080/{}'.format(path)).text
    return render_template("index.html")

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
    return jsonify(data={'randomNumber': randint(1, 100)}, **http_status_response('OK')
                  ), HTTPStatus.OK.value
