import requests

# URL публичного API
url = "https://jsonplaceholder.typicode.com/posts"

# Отправляем GET-запрос
response = requests.get(url)


# Проверяем, что запрос успешен
if response.status_code == 200:
    posts = response.json()

    # Выводим первые 5 постов
    for post in posts[:5]:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)
else:
    print("Ошибка при получении данных:", response.status_code)
