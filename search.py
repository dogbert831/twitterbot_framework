import tweepy
from secrets import *
import json

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    for tweet in tweepy.Cursor(api.search, q="trump tweets", lang="en").items(1):
        print(tweet.text)
    	#print(json.dumps(tweet, sort_keys=True))
    	#if not tweet.retweeted:
            #print(tweet.full_text)


except tweepy.error.TweepError as e:
        log(e.message)
