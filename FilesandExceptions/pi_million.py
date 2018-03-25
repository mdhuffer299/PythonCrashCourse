# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:30:37 2018

@author: mhuffer
"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the first 1 million digits of PI!")
else:
    print("Sorry!!!!")