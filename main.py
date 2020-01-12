import requests
import time
from datetime import datetime

city = input('Enter your City : ')
api_key = Your API Key
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

content = requests.get(url)

data = content.json()
if data:
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    city = data['name']
    current_temp = data['main']['temp']
    desc = data['weather'][0]['description']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sun_rise = data['sys']['sunrise']
    sun_rise = datetime.fromtimestamp(sun_rise)
    sun_rise = sun_rise.strftime('%H:%M:%S')

    sun_set = data['sys']['sunset']
    sun_set = datetime.fromtimestamp(sun_set)
    sun_set = sun_set.strftime('%H:%M:%S')


    print(f'City : {city}')
    print(f'Latitude : {latitude}')
    print(f'Longitude : {longitude}')
    print(f'Current Temperature : {current_temp} degree celcius')
    print(f'Minimum Temperature : {temp_min} degree celcius')
    print(f'Maximum Temperature : {temp_max} degree celcius')
    print(f'Pressure : {pressure} hpa')
    print(f'Humidity : {humidity} %')
    print(f'Wind Speed : {wind_speed} m/s')
    print(f'Sun Rise : {sun_rise}')
    print(f'Sun Set : {sun_set}')

else:
    print(f'No Data found for {city}')