# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:01:35 2018

@author: mhuffer
"""

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
    
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions
# able to produce same output in just one line of code
squares = [value**2 for value in range(1,11)]
print(squares)


for value in range(1,22,2):
    print(value)
    
for value in range(3,31,3):
    print(value)
    
cubes = []
for value in range(1,11):
    print(value**3)
    
cubes = [value**3 for value in range(1,11)]
print(cubes)
    