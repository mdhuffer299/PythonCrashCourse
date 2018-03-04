# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:27:44 2018

@author: mhuffer
"""
# Case examples
name = "ada lovelace"
print(name.title())

new_name = "Ada Lovelace"
print(new_name.upper())
print(new_name.lower())

# Concatenation examples
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")

# Variable concatenation example
message = "Hello, " + full_name.title() + "!"
print(message)

# Including Tab in output
print("Python!")
print("\tPython!")

# Including new line in output
print("Languages: \nPython\nC\nJavaScript")

# combining new line and tab
print("Lanaguages: \n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace, execute in the terminal to see the trailing space
# .rstrip() removes trailing space
# .lstrip() removes leading space
# .strip() removes both leading/trailing spaces
favorite_language = 'python'
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

