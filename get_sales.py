from mongo import MongoDB

def fetch_sale_links():
  db = MongoDB()
  stores = db.query_stores()
  sale_stores = [store["sale_url"] for store in stores if "sale_url" in store]
  with open("websites.txt", "a") as f:
    for store in sale_stores:
      f.write(store + "\n")


if __name__ == "__main__":
  fetch_sale_links()