# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:32:13 2018

@author: mhuffer
"""

# positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about your pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('dog', 'murphy')
describe_pet('N/A', 'N/A')

# Keyword argument: explictly call out the parameters and their values.

describe_pet(animal_type = 'dog', pet_name = 'murphy')

# Default values

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about your pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('murphy')