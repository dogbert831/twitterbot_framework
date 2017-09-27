import requests
import json
import random

def scrape_guardian():
	list = ["racists", "tweets", "staff", "anthem", "best", "NFL" "great", "lies", "crowd", "football", "White House"]
	search = random.choice(list)
	r = requests.get('http://content.guardianapis.com/search?section=us-news&q=trump%20' + search + '&api-key=7d26c29d-abde-4b33-84cf-7dce688e48c5')
	results = r.json()
	tweet = results["response"]["results"][0]["webTitle"]
	url = results["response"]["results"][0]["webUrl"]
	return tweet, url
