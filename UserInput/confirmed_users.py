# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:33:28 2018

@author: mhuffer
"""

# Moving items from one list to another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user unto the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying users: " + current_user.title())
    confirmed_users.append(current_user)
    
# print all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())