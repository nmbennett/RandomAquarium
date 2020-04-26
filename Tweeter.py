# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:27:42 2020

@author: Neil

Tweeting for the very first time
"""

import tweepy
import time
from Aquarium import create_aquarium
from credentials import CONSUMER_KEY
from credentials import CONSUMER_SECRET
from credentials import ACCESS_KEY
from credentials import ACCESS_SECRET
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
tweet_timing = 60 * 60 * 5

while True:
    temp = "\n".join(create_aquarium(5,8))
    api.update_status(temp)
    print(temp)
    time.sleep(tweet_timing)