# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:25:37 2018

@author: mhuffer
"""

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)