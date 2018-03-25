# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:08:34 2018

@author: mhuffer
"""

def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()