# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:22:37 2018

@author: mhuffer
"""

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, 'rb') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        ## Use the messge below to pass the exception to the user.
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        
        ## Use the 'pass' below to have the error fail silently.
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)