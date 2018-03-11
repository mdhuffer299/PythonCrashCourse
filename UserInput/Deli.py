# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:00:09 2018

@author: mhuffer
"""

sandwiches = []
made_sandwiches = []

sandwich_flag = True

while sandwich_flag:
    prompt = "What type of sandwich would you like? "
    sandwich = input(prompt)
    sandwiches.append(sandwich)
        
    while sandwiches:
        current_sandwich = sandwiches.pop()
        print("I have made your " + current_sandwich.title() + " sandwich!")
        made_sandwiches.append(current_sandwich)
        
    repeat = input("Would you llike to make another sandwich? (Y/N) ")
    if repeat == 'N':
        sandwich_flag = False
    
print("\nThe following sandwiches have been made:")
for sand in made_sandwiches:
    print("\t" + sand.title())
