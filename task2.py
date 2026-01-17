import requests

# Введите ваш API-ключ OpenWeather
API_KEY = "ВАШ_API_КЛЮЧ"

# Ввод города от пользователя
city = input("Введите название города: ")

# URL API
url = "https://api.openweathermap.org/data/2.5/weather"


# Параметры запроса
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",   # температура в градусах Цельсия
    "lang": "ru"         # описание погоды на русском
}

# Отправка GET-запроса
response = requests.get(url, params=params)
