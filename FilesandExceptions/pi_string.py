# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:21:26 2018

@author: mhuffer
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))