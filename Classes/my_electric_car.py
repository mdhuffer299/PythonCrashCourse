# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:58:50 2018

@author: mhuffer
"""

from new_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()