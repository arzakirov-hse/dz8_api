import requests

API_KEY = "255793f5cc4b7c0b5e2e936f7cafc1c7"

# Ввод города
city = input("Введите название города: ")

# ---------- 1. Direct Geocoding ----------
geo_url = "http://api.openweathermap.org/geo/1.0/direct"

geo_params = {
    "q": city,
    "limit": 1,
    "appid": API_KEY
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

if not geo_data:
    print("Город не найден")
    exit()

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]

# ---------- 2. Current Weather ----------
weather_url = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
    "lang": "ru"
}

weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

temperature = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]

# ---------- Вывод ----------
print(f"\nГород: {city}")
print(f"Температура: {temperature} °C")
print(f"Погода: {description}")