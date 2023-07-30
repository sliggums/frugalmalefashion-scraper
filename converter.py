import json
from mongo import MongoDB
from algoliasearch.search_client import SearchClient

def convert():
  with open("json/outerknown.json", "r") as f:
    lines = f.read()
    lines_json = json.loads(lines)
    with open("json/outerknown_links.json", "a") as g:
      for product in lines_json:
        if "Info_URL" in product:
          url = product["Info_URL"]
          g.write(url + "\n")

def combine():
  with open("json/outerknown.json", "r") as f:
    with open("json/outerknown_image_urls.json", "r") as g:
      with open("json/outerknown_full.json", "a") as h:
        output = []
        f_lines = f.read()
        f_lines_json = json.loads(f_lines)
        g_lines = g.read()
        g_lines_json = json.loads(g_lines)
        for i in range(len(f_lines_json)):
          a = f_lines_json[i]
          b = g_lines_json[i]
          a["Image"] = b["Image"]
          a["Info"] = a["Info"].split("-")[0]
          output.append(a)
        h.write(str(output))

def upsert_to_mongo():
  db = MongoDB()
  with open("mappings.txt", "r") as mappings:
    mappings_json = json.loads(mappings.read())
    for file_name, field_mappings in mappings_json.items():
      with open("json/" + file_name) as f:
        f_json = json.loads(f.read())
        for item in f_json:
          new_item = dict()
          for k, v in field_mappings.items():
            updated_value = item[k].strip()
            if updated_value == "SOLD OUT" or not updated_value:
              break
            new_item[v] = updated_value
            new_item["site"] = file_name.split(".")[0]

          if len(new_item) - 1 == len(field_mappings):
            db.upsert_item("items", new_item)


def upsert_to_algolia():
  db = MongoDB()
  client = SearchClient.create("0JK5MOYV7L", "cdc1ba4d5b4610337becefff57c9b2b5")

  # Create a new index and add a record
  index = client.init_index("bargains")
  for item in db.query("items"):
    item["objectID"] = str(item["_id"])
    del item["_id"]
    index.save_object(item).wait()

if __name__ == "__main__":
  upsert_to_mongo()
  upsert_to_algolia()
