# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:54:51 2018

@author: mhuffer
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())