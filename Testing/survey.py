# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:35:57 2018

@author: mhuffer
"""

class AnonymousSurvey():
    """Collect anonymous anwsers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the survey questions."""
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response.lower())
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response.title())