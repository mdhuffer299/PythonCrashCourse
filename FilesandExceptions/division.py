# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:52:01 2018

@author: mhuffer
"""

# Basic try-except block
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

# Using an exception to prevent a crash
print("Give me two numbers, and I'll divide them.")
print("Enter 'Q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'Q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'Q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)