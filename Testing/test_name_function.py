# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:17:45 2018

@author: mhuffer
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Michael Dale Huffer' work?"""
        formatted_name = get_formatted_name('michael', 'huffer', 'dale')
        self.assertEqual(formatted_name, 'Michael Dale Huffer')
        
unittest.main()