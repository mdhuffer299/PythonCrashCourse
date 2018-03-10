# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:30:19 2018

@author: mhuffer
"""

# Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with sorted()
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Print a list in reverse order
cars.reverse()
print(cars)

# Simple IF statement example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

