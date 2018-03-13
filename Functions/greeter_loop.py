# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:12:53 2018

@author: mhuffer
"""

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'Q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'Q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'Q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")