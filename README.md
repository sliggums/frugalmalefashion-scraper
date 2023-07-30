# frugalmalefashion-scraper
Script that scrapes r/frugalmalefashion and finds sites with items on clearance.

Then manually uses Octoparse to scrape the items on sale, with their link, image, and prices. These items are stored in MongoDB as a source of truth, and then uploaded to Algolia, where they are served to the webserver.
