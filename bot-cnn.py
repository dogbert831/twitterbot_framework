import os
import tweepy
from secrets import *
from time import gmtime, strftime
import random
import bot

# ====== Individual bot configuration ==========================
bot_username = 'DonaldBotNot'
logfile_name = bot_username + ".log"

# ==============================================================
tweets = [" does it again.", " is unraveling at the seams.", " has no clue does he?", " continues to run off at the mouth.", " is a real tool.", " flips out again."]
rtweet = random.choice(tweets)
with open("results.txt") as f:
    for line in f:
        if "trump" in line:
            lastmatch = line
    if lastmatch is not None:
        url = lastmatch

def create_tweet(url):
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    tweet = "#Dotard" + rtweet
    text = tweet + " " + url
    print(text)
    return text

string = create_tweet(url)
print("text is ", string)
bot.tweet(string)

