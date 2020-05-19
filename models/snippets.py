import datetime
import logging

EXPIRATION_TIME_SECONDS = 30

class SnippetsModel:
    def __init__(self):
        self.cache = {}

    def update_expiration(self, snippet_name):

      current_time = datetime.datetime.now() 
      created_time = self.cache[snippet_name]["created_at"]
      ttl = self.cache[snippet_name]["expires_in"]
      diff = (current_time - created_time).seconds

      if diff > ttl and created_time <= current_time:
        self.delete(snippet_name)
        raise Exception("Sorry, snippet {} has expired and has been purged.".format(snippet_name))
      else:
        new_time = created_time + datetime.timedelta(seconds=EXPIRATION_TIME_SECONDS)
        self.cache[snippet_name]["created_at"] = new_time   
      return self.cache[snippet_name]

    def delete(self, snippet_name):
        del self.cache[snippet_name]
        return

    def put(self, snippet_name):
        try:
            entity = self.cache[snippet_name]
            entity["likes"]+=1
            snippet = self.update_expiration(snippet_name)
            return snippet      
        except KeyError: 
            logging.error("{} does not exist.".format(snippet_name))
            raise Exception("Sorry, snippet {} does not exist.".format(snippet_name))

    def get(self, snippet_name):         
        try:           
            snippet = self.update_expiration(snippet_name)
            return snippet
        except KeyError: 
            logging.error("{} does not exist.".format(snippet_name))
            raise Exception("Sorry, snippet {} does not exist.".format(snippet_name))

    def post(self, snippet_name, value):
        self.cache[snippet_name] = value
        return self.cache[snippet_name]