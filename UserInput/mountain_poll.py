# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:46:55 2018

@author: mhuffer
"""

# Filling a dictionary with User input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ") # Key
    response = input("Which mountain would you like to climb someday? ") # Value
    
    # Store the response in the dictionary
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (Y/N) ")
    if repeat == 'N':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")