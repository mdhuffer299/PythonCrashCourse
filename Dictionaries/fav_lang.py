# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:57:05 2018

@author: mhuffer
"""

# A dictionary of similar objects
fav_languages = {
        'jen': 'python'
        , 'sarah': 'c'
        , 'edward': 'ruby'
        , 'phil': 'python'
        }

print("Sarah's favorite language is " + fav_languages['sarah'].title() + ".")

# looping through all key-value pairs
user_0 = {
        'username': 'efermi'
        ,'first': 'enrico'
        ,'last': 'fermi'
        }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    
fav_languages = {
        'jen': 'python'
        , 'sarah': 'c'
        , 'edward': 'ruby'
        , 'phil': 'python'
        }

for name, language in fav_languages.items():
    print(name.title() + "'s favorite language is: " + language.title() + "!")
    
for name in fav_languages.keys():
    print(name.title())
    
# Selecting a particular item in a dictionary
friends = ['phil', 'sarah']
for name in fav_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              fav_languages[name].title() + "!")
        
if 'erin' not in fav_languages.keys():
    print("Erin, please take our poll!")
    
# Looping through a dictionary's keys in order
for name in sorted(fav_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")
    
# Looping through all values in a dictionary
# can produce duplicates
print("The following languages have been mentioned: ")
for language in fav_languages.values():
    print("\t" + language.title() + "!")
    
# Using a set to create a distinct list of records
print("The following languages have been mentioned: ")
for language in set(fav_languages.values()):
    print("\t" + language.title() + "!")
    
favorite_languages = {
        'jen': ['python', 'ruby']
        , 'sarah': ['c']
        , 'edward': ['ruby', 'go']
        , 'phil': ['python', 'haskell']
        }

for name, langs in favorite_languages.items():
    if len(langs) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for lang in langs:
            print("\t" + lang.title())
    else:
        print("\n" + name.title() + "'s favorite language is:")
        for lang in langs:
            print("\t" + lang.title())