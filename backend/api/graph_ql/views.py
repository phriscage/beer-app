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
from flask_graphql import GraphQLView
from graphene import Schema

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/../../')

from lib.utils import http_status_response # noqa
from lib.wrapper import get_beer_details, get_beer_reviews # noqa
from lib.schema import Query # noqa

logger = logging.getLogger(__name__)
graphql = Blueprint('graphql', __name__)


view_func = GraphQLView.as_view(
    'graphql', schema=Schema(query=Query), graphiql=True)

graphql.add_url_rule('', view_func=view_func)
