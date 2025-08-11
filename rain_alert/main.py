"""
day 35: rain alert

API authentication
"""
import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv() # Loading environment variables

# Email Config
EMAIL_PORT = 587
TIMEOUT = 120
FROM = SENDER_EMAIL='chukwuemekalearning@gmail.com'
TO = RECEIVER_EMAIL='chukwuemekangumoha@proton.me'
LOGIN_PASSWORD = os.environ.get('EMAIL_APP_PASSWORD')

# OpenWeatherMap API details
API_KEY = os.environ.get('OWM_API_KEY')
MY_LAT = 8.495750
MY_LONG = 8.521550
# api.openweathermap.org/data/2.5/forecast?lat=9.076479&lon=7.398574&appid=c75aa333e96e19a61b475c1decf95ad7
API_URL = f'https://api.openweathermap.org/data/2.5/forecast'

params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(API_URL, params=params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])
will_rain = False
for data_pt in weather_data['list']:
    code = data_pt['weather'][0]['id']
    if code < 700:
        will_rain = True

if will_rain:
    # Due to issues with Twilio API,
    # Send an email instead of SMS
    with smtplib.SMTP('smtp.gmail.com', port=EMAIL_PORT, timeout=TIMEOUT) as conn:
        conn.starttls()
        conn.login(user=FROM, password=LOGIN_PASSWORD)
        conn.sendmail(
            from_addr=FROM,
            to_addrs=TO,
            msg='Subject: Rain Alert\n\n'
                'It\'s going to rain today. Please remember to bring an umbrella'
        )