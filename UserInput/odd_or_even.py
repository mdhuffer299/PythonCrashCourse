# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:32:28 2018

@author: mhuffer
"""

number = input("Enter a number, and I'll tell you if it is even or odd: ")
number = int(number)

if number % 2 ==  0:
    print("The number " + str(number) + " is an even number!")
else:
    print("The number " + str(number) + " is an odd number!")