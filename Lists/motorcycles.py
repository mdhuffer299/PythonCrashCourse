# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:17:38 2018

@author: mhuffer
"""

# Modifying a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles.append('honda')
print(motorcycles)

# Start with empty list and build the list dynamically!
motorcycles_new = []
print(motorcycles_new)

motorcycles_new.append('honda')
print(motorcycles_new)
motorcycles_new.append('yamaha')
print(motorcycles_new)
motorcycles_new.append('suzuki')

print(motorcycles_new)

# insert elements into a list
motorcycles_new.insert(0, 'ducati')
print(motorcycles_new)

# removing elements from a list
del motorcycles_new[0]
print(motorcycles_new)

del motorcycles_new[1]
print(motorcycles_new)

# pop() method
motorcycles_pop = ['honda', 'yamaha', 'suzuki']
print(motorcycles_pop)

popped_motorcycle = motorcycles_pop.pop()
print(motorcycles_pop)
print(popped_motorcycle)

last_owned = motorcycles_pop.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# able to pop any element from a list.  Just need to define the index of the element
first_owned = motorcycles_pop.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# removing an item by value
motorcycles_value = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_value)
motorcycles_value.remove('ducati')
print(motorcycles_value)

# use variable to remove item from list
motorcycles_var_value = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_var_value)

too_expensive = 'ducati'
motorcycles_var_value.remove(too_expensive)
print(motorcycles_var_value)
print("\nA " + too_expensive.title() + " is too expensive for me.")