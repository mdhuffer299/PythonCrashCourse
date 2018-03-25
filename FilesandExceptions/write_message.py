# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:35:31 2018

@author: mhuffer
"""

filename = 'programming.txt'

# Write to a file
#with open(filename, 'w') as file_object:
#    file_object.write("I love programming.\n")
#    file_object.write("I love creating new game.\n")
    
# Append text to a file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")