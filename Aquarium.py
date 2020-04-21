# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:17:56 2020

@author: Neil

Making an emoji aquarium
"""

import emoji
from random import randint

'''
#Livestock
print("\U0001F41F")#fish
print("\U0001F420")#Tropical fish
print("\U0001F40B")#whale
print("\U0001F433")#whale two
print("\U0001F40C")#snail
print("\U0001F42C")#dolphin
print("\U0001F419")#squid
print("\U0001F438")#frog
print("\U0001F422")#turtle
print("\U0001F421")#blowfish
print("\U0001F990")#shrimp
print("\U0001F980")#crab
print("\U0001F99E")#lobster
print("\U0001F991")#squid
print("\U0001F9AA")#oyster

#Tank Bottom
print("\U0001F40C")#snail
print("\U0001F9AA")#oyster
print("\U0001F331")#seedling
print("\U0001F33F")#herb
print("\U0001F33E")#ear of rice
print("\U00002618")#shamrock
print("\U0001F340")#four leaf clover
print("\U00002693")#anchor
print("\U0001F531")#trident
print("\U0001F5FF")#moai
'''

tank_bottom_options = [" "," "," "," "," "," "," "," "," "," "," ",
                       "\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F33F",
                       "\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F331",
                       "\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F",
                       "\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F",
                       "\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E",
                       "\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E",
                       "\U0001F40C", "\U00002693","\U0001F5FF" ]

livestock_options = [" "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                     " "," "," "," "," "," "," "," "," "," "," ",
                "\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F",
                "\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F",
                "\U0001F420","\U0001F420","\U0001F420","\U0001F420","\U0001F420",
                "\U0001F420","\U0001F420","\U0001F420","\U0001F420","\U0001F420",
                "\U0001F421","\U0001F421","\U0001F421","\U0001F421","\U0001F421",
                "\U0001F421","\U0001F421","\U0001F421","\U0001F421","\U0001F421",
                "\U0001F990","\U0001F990","\U0001F990","\U0001F990","\U0001F990",
                "\U0001F990","\U0001F990","\U0001F990","\U0001F990","\U0001F990",
                "\U0001F40C","\U0001F40C","\U0001F40C","\U0001F40C","\U0001F40C",
                "\U0001F40B","\U0001F433","\U0001F42C","\U0001F419","\U0001F438",
                "\U0001F422","\U0001F980","\U0001F99E","\U0001F991"]

only_livestock = ["\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F",
                "\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F","\U0001F41F",
                "\U0001F420","\U0001F420","\U0001F420","\U0001F420","\U0001F420",
                "\U0001F420","\U0001F420","\U0001F420","\U0001F420","\U0001F420",
                "\U0001F421","\U0001F421","\U0001F421","\U0001F421","\U0001F421",
                "\U0001F421","\U0001F421","\U0001F421","\U0001F421","\U0001F421",
                "\U0001F990","\U0001F990","\U0001F990","\U0001F990","\U0001F990",
                "\U0001F990","\U0001F990","\U0001F990","\U0001F990","\U0001F990",
                "\U0001F40C","\U0001F40C","\U0001F40C","\U0001F40C","\U0001F40C",
                "\U0001F40B","\U0001F433","\U0001F42C","\U0001F419","\U0001F438",
                "\U0001F422","\U0001F980","\U0001F99E","\U0001F991","\U0001F9AA"]

tank_bottom = []

def create_aquarium(height, width):
    water = height - 1
    tank = [[] for i in range(0, height)]
    
    for indx in range(water):
        for num in range(width):
             tank[indx].append(livestock_options[randint(0,len(livestock_options)-1)])
        
        
    for num in range(width):
        tank[height-1].append(tank_bottom_options[randint(0,len(tank_bottom_options)-1)])

   
    tank[0][0] = only_livestock[randint(0,len(only_livestock)-1)]
          
    tank = [''.join(tank[i]) for i, item in enumerate(tank)]
    
    return tank




