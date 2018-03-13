# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:41:21 2018

@author: mhuffer
"""

def build_person(first_name, last_name, age = ''):
    """Return a dictonary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return(person)

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)