# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:11:59 2018

@author: mhuffer
"""

from name_function import get_formatted_name

print("Enter 'Q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'Q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'Q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")