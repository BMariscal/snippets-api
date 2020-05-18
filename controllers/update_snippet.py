from .process_payload import process_entity
from models import db

def update(snippet_name):
  store = db.STORE
  existing_entity = store.put(snippet_name)
  snippet = process_entity(existing_entity)
  return snippet