# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:17:56 2020

@author: Neil

Making an emoji aquarium
"""

from random import sample

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

tank_bottom_options = ["    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "    ","    ","    ","    ","    ","    ","    ",
                       "\U000E0020","\U000E0020","\U000E0020","\U000E0020","\U000E0020","\U000E0020","\U000E0020",
                       "\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F331","\U0001F331",
                       "\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F",
                       "\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F","\U0001F33F",
                       "\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E",
                       "\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E","\U0001F33E",
                       "\U0001F40C", "\U00002693","\U0001F5FF" ]

livestock_options = ["    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
                     "    ","    ","    ","    ","    ","    ","    ",
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
    
    tank[0].append(''.join(sample(only_livestock,1)))
    tank[0].append(''.join(sample(livestock_options,width-1)))

    for indx in range(1,water):
        tank[indx].append(''.join(sample(livestock_options,width)))

    tank[height-1].append(''.join(sample(tank_bottom_options,width)))
       
          
    tank = [''.join(tank[i]) for i, item in enumerate(tank)]
    
    return tank
