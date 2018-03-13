# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:28:41 2018

@author: mhuffer
"""

# Start with some designs taht need to be printed.
unprinted_designs = ['iphone case', 'robot perndant', 'dodecahedron']
completed_models = []

# First step: 
# Simulate printing each design, until none are left
# Move each design to completed_models after printing.
"""
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print("\t" + completed_model.title())
"""

# Function creation Step 2:
    
# handles the printing of the designs
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
# summarize the prints that have been made
def show_completed_models(completed_models):
    """ Show all the models that were printed. """
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print("\t" + completed_model.title())
        
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)