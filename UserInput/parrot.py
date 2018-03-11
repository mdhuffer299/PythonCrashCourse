# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:26:20 2018

@author: mhuffer
"""

prompt = "Hello, tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active_flag = True
while active_flag == True:
    message = input(prompt)
    
    if message == 'quit':
        active_flag = False
    else:
        print(message)