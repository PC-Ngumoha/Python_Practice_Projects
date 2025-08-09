"""
day 35: rain alert

API authentication
"""
import requests
from sendchamp import Sendchamp
# from twilio.rest import Client

# OpenWeatherMap API details
API_KEY = 'c75aa333e96e19a61b475c1decf95ad7'

# # Twilio API config
# account_sid = 'ACaf16f0b376abaf9ffd6c020f6fde01c5'
# auth_token = '23c78cff53e74016096669aab5aec9dd'

# SendChamp config
SENDCHAMP_KEY = 'sendchamp_live_$2a$10$chKtGKHPZ5nX0Hzx8gQY5.AjWICEHAvbqkF73mXQuL3BTMscJr2bG'


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
    # # TWILIO CODE
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella",
    #     from_="+16187536221",
    #     to="+2347089699162",
    # )
    #
    # print(message.status) # Verify that SMS sent successfully.

    # SENDCHAMP
    client = Sendchamp(SENDCHAMP_KEY)
    response = client.sms.send(
        to=['+2347089699162'],
        message='It\'s going to rain today. Remember to bring an umbrella.',
        sender_name="Sendchamp",
        route="international"
    )
    print(response)