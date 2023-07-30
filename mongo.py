import os
import pymongo

class MongoDB:
  def __init__(self):
    connection_string = os.getenv("MONGO_CONNECTION_STRING")
    self.client = pymongo.MongoClient(connection_string, connect=False)
    database_name = "fmf"
    self.database_name = self.client[database_name]

  def __exit__(self):
    if self.client:
      self.client.close()

  def query_stores(self):
    try:
      collection_name = "store_sites"
      collection = self.database_name[collection_name]
      output = collection.find()
      return list(output)
    except Exception as e:
      print(e)

  def upsert(self, collection_name, **kwargs):
    try:
      collection = self.database_name[collection_name]
      filtered_fields = {k:v for k, v in kwargs.items() if v}
      collection.insert_one(filtered_fields)
    except Exception as e:
      print(e)

  def upsert_item(self, collection_name, item):
    try:
      collection = self.database_name[collection_name]
      filtered_fields = {k:v for k, v in item.items() if v}
      collection.insert_one(filtered_fields)
    except Exception as e:
      print(e)
      raise e

# if __name__ == "__main__":
#   db = MongoDB()
#   db.upsert_stores(test="hi", test2=None)
#   db.query_stores()