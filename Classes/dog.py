# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:41:39 2018

@author: mhuffer
"""

class Dog():
    """ A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """ Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """ Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
# Creating a single instance
my_dog = Dog('murphy' , 2)
my_dog.sit()
my_dog.roll_over() 

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Creating multiple instances
moms_dog = Dog('gonzo', 9)
dads_dog = Dog('bogey', 7)

moms_dog.sit()
moms_dog.roll_over() 

print("\nMy moms dog name is " + moms_dog.name.title() + ".")
print("My moms dog is " + str(moms_dog.age) + " years old.")

dads_dog.sit()
dads_dog.roll_over() 

print("\nMy dads dog name is " + dads_dog.name.title() + ".")
print("My dads dog is " + str(dads_dog.age) + " years old.")