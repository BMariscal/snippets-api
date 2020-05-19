import datetime

from .process_payload import process_entity
from models import db


def valid_input(data):
  if not ("name" in data and "expires_in" in data and "snippet" in data):
    return False
  return True

def create(data):
  if not valid_input(data):
    raise Exception("Invalid input.")

  snippet_data = {
    "name": "",
    "created_at": datetime.datetime.now(),
    "expires_in": 0,
    "snippet": "",
    "likes": 0
  } 
  snippet_data["name"] = data["name"]
  snippet_data["expires_in"] = data["expires_in"]
  snippet_data["snippet"] = data["snippet"]

  store = db.STORE
  created_entity = store.post(snippet_data["name"], snippet_data)
  entity = process_entity(created_entity)
  return entity






