# """
# day 35: rain alert
#
# API authentication
# """
# import requests
# from twilio.rest import Client
#
# # OpenWeatherMap API details
#
# MY_LAT = 8.495750
# MY_LONG = 8.521550
# # api.openweathermap.org/data/2.5/forecast?lat=9.076479&lon=7.398574&appid=c75aa333e96e19a61b475c1decf95ad7
# API_URL = f'https://api.openweathermap.org/data/2.5/forecast'
#
# params = {
#     'lat': MY_LAT,
#     'lon': MY_LONG,
#     'appid': API_KEY,
#     'cnt': 4,
# }
#
# response = requests.get(API_URL, params=params)
# response.raise_for_status()
# weather_data = response.json()
# # print(weather_data['list'][0]['weather'][0]['id'])
# will_rain = False
# for data_pt in weather_data['list']:
#     code = data_pt['weather'][0]['id']
#     if code < 700:
#         will_rain = True
#
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="It's going to rain today. Remember to bring an umbrella",
#         from_="+16187536221",
#         to="+2347089699162",
#     )
#
#     print(message.status) # Verify that SMS sent successfully.