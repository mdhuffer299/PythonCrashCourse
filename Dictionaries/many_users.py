# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:07:42 2018

@author: mhuffer
"""

# A dictionary in a dictionary
users = {
        'aeinstein': {
                'first': 'albert'
                ,'last': 'einstein'
                ,'location': 'princeton'
                }
        ,'mcurie': {
                'first': 'marie'
                ,'last': 'curie'
                ,'location': 'paris'
                }
        }
        
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())