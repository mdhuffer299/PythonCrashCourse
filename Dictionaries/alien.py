# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:55:21 2018

@author: mhuffer
"""
# Example Dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding items to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 15
print(alien_1)

# Modify values in a dictionary
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The modified alien is " +alien_0['color'] + ".")

alien_2 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_2['x_pos']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 5
elif alien_2['speed'] == 'fast':
    x_increment = 10
else:
    print("No alien found!")
    
alien_2['x_pos'] = alien_2['x_pos'] + x_increment
print("New x-position: " + str(alien_2['x_pos']))

# Removing key-value pairs
del alien_0['points']
print(alien_0)
