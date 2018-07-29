from graphene import ObjectType, List, String, Boolean, ID, Field, Int
from graphene.types.datetime import DateTime
from .wrapper import get_beer_details, get_beer_reviews # noqa
from flask import jsonify
from collections import namedtuple
import simplejson as json
import logging

logger = logging.getLogger(__name__)

class Beer(ObjectType):
    id = ID()
    brewery = String()
    name = String()
    price = String()
    style = String()
    reviews: List(lambda: Review)
    created_at = DateTime()
    updated_at = DateTime()

class User(ObjectType):
    id = ID()
    name = String()

class Review(ObjectType):
    id = ID()
    text = String()
    beer = Field(lambda: Beer)
    reviewer = Field(lambda: User)
    created_at = DateTime()
    updated_at = DateTime()

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

class Query(ObjectType):
   beer = Field(Beer, id=Int(required=True))
   beers = List(Beer, id=String(required=True))

   def resolve_beer(self, info, **args):
      #logger.debug(info.context)
      status, details = get_beer_details(args.get("id"), info.context.headers, info.context.query_string)
      logger.debug(type(details.get("data")))
      logger.debug(_json_object_hook(details.get("data")))
      return _json_object_hook(details.get("data"))

   def resolve_beers(self, args, context, info):
      #beers = api_call(args.get("id"))["reviews"]
      logger.debug('resolve_beers: testsssts')
      beers = get_beer_details(None, None, args)
      return json.dumps(beers)
