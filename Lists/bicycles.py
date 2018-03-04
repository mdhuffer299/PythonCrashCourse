# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:01:14 2018

@author: mhuffer
"""

# Good idea to make name of list plural, as it contains more than one item.
bicycles = ['trek' , 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing specific items in the list
print(bicycles[0])

# You can also add string methods to the items of a list if the output is a string
print(bicycles[0].title())

# python indexing starts at 0, must refer to nth item by the n - 1 index
print(bicycles[2])
print(bicycles[3])

# Python offers a special syntax to retrieve the last element in a list
print(bicycles[-1])

# Use individual values from a list example
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)