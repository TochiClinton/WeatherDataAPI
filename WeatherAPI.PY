import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "1486986d3ab6d30cb8e9190e352ca0fc"
CITY = "Lagos"


def kelvin_to_celsius_to_fahrenheit(kelvin):
    celsuis = kelvin - 273.15
    fahrenheit = celsuis * (9/5) + 32
    return celsuis, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)

temp_kelvin = response['main']['temp']
temp_celsuis, temp_fahrenheit = kelvin_to_celsius_to_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsuis, feels_like_fahrenheit = kelvin_to_celsius_to_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']


humidity =  response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Tempereture in {CITY}: {temp_celsuis:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Tempereture in {CITY} feels like: {feels_like_celsuis:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Windspeed in {CITY}: {wind_speed}m/s")
print(f"General Weaather in {CITY}: {description}")
print(f"Sun Rises in {CITY} at {sunrise_time} local time.")
print(f"Sun Sets in {CITY} at {sunset_time} local time.")
