# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:25:31 2018

@author: mhuffer
"""

def greet_user(name):
    """Display a simple greeting."""
    print("Hello! " + name)

name = input("What is you name? ")

greet_user(name)