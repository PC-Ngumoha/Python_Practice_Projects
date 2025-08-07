"""
Day 33: APIs
main.py: entry point file
"""
import requests
from datetime import datetime

# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status() # Raise exception based on status code
#
# data = response.json()
# lat = data['iss_position']['latitude']
# long = data['iss_position']['longitude']
# coord = (lat, long)
# print(f"Coordinates: {coord}")

# CONSTANTS
MY_LAT = 9.076479
MY_LONG = 7.398574

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json',
                        params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
