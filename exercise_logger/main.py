"""
Exercise Logger main codebase.

Nutritionix API: Chukwuemeka Ngumoha's App

—
"""
import os
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

# Headers for authentication
auth_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

# API URLs
NUTRITIONIX_EXERCISE_API_URL = os.environ.get('NUTRITIONIX_EXERCISE_API_URL')
SHEETY_API_URL = os.environ.get('SHEETY_API_URL')
SHEETY_AUTH_USERNAME = os.environ.get('SHEETY_AUTH_USERNAME')
SHEETY_AUTH_PASSWORD = os.environ.get('SHEETY_AUTH_PASSWORD')

activity = input('What did you get done: ')

body = {
    'query': activity
}

response = requests.post(NUTRITIONIX_EXERCISE_API_URL, headers=auth_headers, json=body)
response.raise_for_status()
exercises = response.json()['exercises']

if len(exercises) > 0: # The user actually did something
    for exercise in exercises:
        right_now = datetime.now()
        body = {
            'workout': {
                'date': right_now.strftime('%d/%m/%Y'),
                'time': right_now.strftime('%X'),
                'exercise': exercise['name'].title(),
                'duration': float(exercise['duration_min']),
                'calories': float(exercise['nf_calories']),
            }
        }
        sheety_header = {
            'Content-Type': 'application/json',
        }

        # Make a request to add entry to Google sheets
        sheety_response = requests.post(SHEETY_API_URL, json=body,
                                        auth=(SHEETY_AUTH_USERNAME, SHEETY_AUTH_PASSWORD))
        sheety_response.raise_for_status()
    print('Exercises successfully logged')
else:
    print('No exercises to log. Have a nice day 👋🏾')
