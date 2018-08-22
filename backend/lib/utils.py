# pylint: disable=broad-except,invalid-name
"""
    Flask API Utils
"""
import os
import sys
from http import HTTPStatus
import functools
import logging
import socket
from datetime import datetime
import simplejson as json

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../../')

logger = logging.getLogger(__name__)


def get_fqdn():
    """ get the default fqdn with socket """
    return socket.getfqdn()


def get_ip_address():
    """ get the default ip_address with socket """
    try:
        return socket.gethostbyname(socket.getfqdn())
    except socket.gaierror as error:
        logger.warning(error)
    return socket.gethostbyname("")


def http_status_response(enum_name):
    """ create a custom HTTPStatus response dictionary """
    if not getattr(HTTPStatus, enum_name):
        return {}
    return {
        'code': getattr(HTTPStatus, enum_name).value,
        'status': getattr(HTTPStatus, enum_name).phrase,
        'description': getattr(HTTPStatus, enum_name).description
    }


def rsetattr(obj, attr, val):
    """ dynamically set obj attr """
    pre, _, post = attr.rpartition('.')
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)

sentinel = object()


def rgetattr(obj, attr, default=sentinel):
    if default is sentinel:
        _getattr = getattr
    else:
        def _getattr(obj, name):
            return getattr(obj, name, default)
    return functools.reduce(_getattr, [obj]+attr.split('.'))


def get_forward_headers(request, whitelist=None):
    """ set the appopriate forwarding headers for Istio service """
    headers = {}
    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]
    if whitelist and type(whitelist) is list:
        incoming_headers += whitelist
    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
    return headers


class PythonObjectEncoder(json.JSONEncoder):
    """ custom json.JSONEncoder for requests """

    def default(self, obj):
        """ default method """
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return json.JSONEncoder.default(self, obj)
        if isinstance(obj, datetime):
            return obj.isoformat() + 'Z'
            #return str(obj)
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
