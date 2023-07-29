from mongo import MongoDB
import praw
import re
import os

def get_subdomain(url):
  """Gets the domain of a URL.

  Args:
    url: The URL to get the domain of.

  Returns:
    The domain of the URL.
  """

  match = re.match(r"(.*?)\.(.*?)\.(.*)", url)
  return match.group(2) if match else None

def fetch_all_posts(subreddit_name):
  db = MongoDB()
  client_id = os.getenv("REDDIT_CLIENT_ID")
  client_secret = os.getenv("REDDIT_CLIENT_SECRET")
  reddit = praw.Reddit(client_id=client_id,
                      client_secret=client_secret,
                      user_agent="FMF crawler")
  subreddit = reddit.subreddit(subreddit_name)
  posts = subreddit.new(limit=None)

  #existing_stores = set(db.query_stores())
  existing_stores = set()

  for post in posts:
    subdomain = get_subdomain(post.url)
    if post.url and "redd" not in post.url and subdomain not in existing_stores:
      sale_url = post.url if "sale" in post.url or "clearance" in post.url else None
      db.upsert_stores(url=post.url, sale_url=sale_url, subdomain=subdomain)
      existing_stores.add(subdomain)

if __name__ == "__main__":
  fetch_all_posts("frugalmalefashion")