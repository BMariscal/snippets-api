import datetime

URL = "https://Snippets-API.briceidamariscal.repl.co/snippets/"

def process_entity(data):
  expire_time = datetime.timedelta(seconds=data["expires_in"])
  created_time = data["created_at"]
  entity = { 
    "name" : data["name"],
    "snippet": data["snippet"],
    "likes" : data["likes"],
  }
  entity["url"] = URL + entity["name"]
  entity["expires_at"] = (created_time + expire_time).isoformat()
  return entity