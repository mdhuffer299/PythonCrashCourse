# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:38:58 2018

@author: mhuffer
"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)