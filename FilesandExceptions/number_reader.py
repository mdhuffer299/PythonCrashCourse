# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:41:14 2018

@author: mhuffer
"""

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)