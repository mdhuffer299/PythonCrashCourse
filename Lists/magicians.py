# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:44:01 2018

@author: mhuffer
"""

# looping through a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
for i in magicians:
    print(i.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + i.title() + ".\n")
    
print("Thank you, everyone. that was a great magic show!")

# Using the range() function
for value in range(1,6):
    print(value)
    
numbers = list(range(1,6))
print(numbers)