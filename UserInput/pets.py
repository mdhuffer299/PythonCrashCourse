# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:41:58 2018

@author: mhuffer
"""

# Removing all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)