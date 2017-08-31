import requests
import json
def scrape_guardian():
    r = requests.get('http://content.guardianapis.com/search?section=us-news&q=trump%20tweets&api-key=7d26c29d-abde-4b33-84cf-7dce688e48c5')
    results = r.json()
    tweet = results["response"]["results"][0]["webTitle"]
    url = results["response"]["results"][0]["webUrl"]
    return tweet, url

