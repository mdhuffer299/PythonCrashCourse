# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:14:26 2018

@author: mhuffer
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    
print('\n')
        
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())