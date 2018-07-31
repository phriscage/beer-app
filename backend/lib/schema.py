# pylint: disable=broad-except,invalid-name,import-error,wrong-import-position,unused-argument
"""
    schema file contains all the GraphQL definitions and objects.
    We leverage the same methods of the RESTful Flask blueprints
"""
import logging
from collections import namedtuple
from graphene import ObjectType, List, String, ID, Field, Int
from graphene.types.datetime import DateTime
import simplejson as json

from .wrapper import get_beer_details, get_beer_reviews # noqa

logger = logging.getLogger(__name__)


def _json_object_hook(d):
    """ required to transform dictionary to objects """
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    """ load json with object_hook """
    return json.loads(data, object_hook=_json_object_hook)


class Review(ObjectType):
    """ Review GraphQL ObjectType """
    id = ID()
    text = String()
    reviewer = Field(lambda: User)
    created_at = DateTime()
    updated_at = DateTime()

    def resolve_reviewer(self, info):
        """ return the Reviewer object """
        return _json_object_hook(self.reviewer)


class Beer(ObjectType):
    """ Beer GraphQL ObjectType """
    id = ID()
    brewery = String()
    name = String()
    price = String()
    style = String()
    reviews = List(lambda: Review)
    created_at = DateTime()
    updated_at = DateTime()

    def resolve_reviews(self, info, **args):
        """ return the child Reviews as list of objects """
        status, reviews = get_beer_reviews(self.id, {}, args)
        if reviews.get("data", None):
            return [_json_object_hook(val) for val in reviews.get("data")]
        return []


class User(ObjectType):
    """ User GraphQL ObjectType """
    id = ID()
    name = String()


class Query(ObjectType):
    """ Query GraphQL ObjectType """
    beer = Field(Beer, id=Int(required=True))
    beers = List(Beer, limit=Int())

    def resolve_beer(self, info, **args):
        """ return the Beer details as object """
        #logger.debug(info.context)
        status, details = get_beer_details(args.get("id"), info.context.headers, args)
        return _json_object_hook(details.get("data")) # named tuple

    def resolve_beers(self, info, **args):
        """ return the Beer details as list of objects """
        status, details = get_beer_details(None, {}, args)
        if details.get("data", None):
            return [_json_object_hook(val) for val in details.get("data")]
        return []
