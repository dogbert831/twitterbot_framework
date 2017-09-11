import os
import tweepy
from secrets import *
from time import gmtime, strftime
import guardian_content
import bot

# ====== Individual bot configuration ==========================
bot_username = 'DonaldBotNot'
logfile_name = bot_username + ".log"

# ==============================================================


def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    ttweet = guardian_content.scrape_guardian()
    tweet = ttweet[0]
    url = ttweet[1]
    text = tweet + " " + url
    #print(text)
    return text

bot.tweet(text)
