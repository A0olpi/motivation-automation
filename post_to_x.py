import tweepy
import json
import os
import random
import time

# Load Twitter API credentials from environment variables
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Load today's content
with open('content.json', 'r') as f:
    content = json.load(f)

# Post to Twitter
try:
    api.update_status(content['full_post'])
    print(f"Successfully posted to X: {content['quote']}")
except Exception as e:
    print(f"Error posting to X: {e}")
