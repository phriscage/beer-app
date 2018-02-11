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
health = Blueprint('health', __name__)


def get_debug_info():
    """ get some debug info """
    return {
        'host': {
            'fqdn': get_fqdn(),
            'ip_address': get_ip_address()
        },
        'request': {
            'url': request.url,
            'headers': dict(request.headers)
        }
    }

def sample_response(extra_data=None):
    """ sample response that is used for all resources """
    # logger.debug(request.headers.environ)
    data = get_debug_info()
    data.update({'extra_data': extra_data})
    return jsonify(data=data, **http_status_response('OK')
                  ), HTTPStatus.OK.value

@health.route('/test', methods=['GET'])
def test():
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
    return sample_response()

@health.route('', methods=['GET'])
def index():
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
    if request.args.get('debug', None):
        data = get_debug_info()
        return jsonify(message="All is well!", data=data, **http_status_response('OK')
                      ), HTTPStatus.OK.value
    return jsonify(message="All is well!", **http_status_response('OK')
                  ), HTTPStatus.OK.value
