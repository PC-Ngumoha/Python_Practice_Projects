"""
Day 33: APIs
main.py: entry point file
"""
import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status() # Raise exception based on status code

data = response.json()
lat = data['iss_position']['latitude']
long = data['iss_position']['longitude']
coord = (lat, long)
print(f"Coordinates: {coord}")