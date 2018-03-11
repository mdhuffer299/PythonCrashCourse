# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:28:48 2018

@author: mhuffer
"""

# Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
    
# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1
    
# This loop runs for ever
# Uncomment if you wish to see, crtl+c to exit loop
#x = 1
#while x <= 5:
#    print(x)