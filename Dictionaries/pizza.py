# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:55:35 2018

@author: mhuffer
"""

# putting a list in a dictionary

# Store information about a pizze being ordered.
pizza = {
        'crust': 'thick'
        ,'toppings': ['mushrooms', 'extra cheese']
        }

# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping.title())