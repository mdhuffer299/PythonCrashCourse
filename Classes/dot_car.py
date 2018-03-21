# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:03:39 2018

@author: mhuffer
"""

import new_car

my_car = new_car.Car('subaru', 'forester', 2017)
print(my_car.get_descriptive_name())

my_dream = new_car.ElectricCar('jaguar', 'electric', 2025)
print(my_dream.get_descriptive_name())