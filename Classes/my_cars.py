# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:01:17 2018

@author: mhuffer
"""

from new_car import Car
from electric_car import ElectricCar

my_bettle = Car('volkswagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())