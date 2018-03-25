# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:43:08 2018

@author: mhuffer
"""

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username.lower(), f_obj)
    return username
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember when you come back, " + username.title() + "!")
            
greet_user()