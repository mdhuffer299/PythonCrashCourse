# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:41:30 2018

@author: mhuffer
"""

# Nesting

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 1}
alien_1 = {'color': 'red', 'points': 2}
alien_2 = {'color': 'yellow', 'points': 3}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# create a fleet of aliens using the range() function

# Make an empty list for storing aliens.
aliens =[]

# make 30 green aliens
for alien_numbers in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# Modify the first three aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        
for alien in aliens[:5]:
    print(alien)
    
# Modify the first three aliens
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
        
for alien in aliens[:10]:
    print(alien)