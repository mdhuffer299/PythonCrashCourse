# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:54:04 2018

@author: mhuffer
"""

from new_car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()