import requests

# URL публичного API
url = "https://jsonplaceholder.typicode.com/posts"

# Отправляем GET-запрос
response = requests.get(url)