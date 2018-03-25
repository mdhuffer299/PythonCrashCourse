# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:48:35 2018

@author: mhuffer
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymouseSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set off responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0].lower(), self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Test that three responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response.lower(), self.my_survey.responses)

unittest.main()