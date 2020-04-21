# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:27:42 2020

@author: Neil

Tweeting for the first time
"""

import tweepy, sys
from Aquarium import create_aquarium
from random import randint
from credentials import CONSUMER_KEY
from credentials import CONSUMER_SECRET
from credentials import ACCESS_KEY
from credentials import ACCESS_SECRET

#argfile = str(sys.argv[1])


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


api.update_status("\n".join(create_aquarium(randint(4,6),randint(7,10))))


'''
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes

print("\U0001F44B","\U0001F30D", "!")
'''


'''
    tank = np.array([item for items in tank for item in items])    
    tank = tank.reshape(height,width)
    tank = '\n'.join(map(str, tank))
    '''