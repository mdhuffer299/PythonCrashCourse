# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:40:43 2018

@author: mhuffer
"""

from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'Q' at anytime to quit.")
while True:
    response = input("Language: ")
    if response == 'Q':
        break
    else:
        my_survey.store_response(response)
        
# Show the results of the survey.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()