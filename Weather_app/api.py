# api.py
import requests
import datetime

def get_weather(city, api_key):
  url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
  response = requests.get(url.format(city, api_key))
  if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    country = data['sys']['country']
    temp_celsius = data['main']['temp']
    weather_desc = data['weather'][0]['description'].capitalize()
    icon_code = data['weather'][0]['icon']
    weather_main = data['weather'][0]['main']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return city_name, country, temp_celsius, weather_desc, icon_code, weather_main, humidity, wind_speed
  else:
    return None

def get_forecast(city, api_key):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  forecast_list = []
  if response.status_code == 200:
    data = response.json()
    for entry in data['list']:
      if '12:00:00' in entry['dt_txt']:
        date = entry['dt_txt'].split()[0]
        temp = entry['main']['temp']
        desc = entry['weather'][0]['description'].capitalize()
        forecast_list.append(f'{date}: {temp}°C, {desc}')
  return forecast_list

def get_hourly_chart_data(city, api_key):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  times, temps = [], []
  if response.status_code == 200:
    data = response.json()
    for entry in data['list'][:8]:
      dt = datetime.datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
      times.append(dt.strftime('%H:%M'))
      temps.append(entry['main']['temp'])
  return times, temps
