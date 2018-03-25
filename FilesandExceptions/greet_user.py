# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:45:08 2018

@author: mhuffer
"""

import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")