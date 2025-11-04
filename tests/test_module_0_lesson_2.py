def greet(name):
    return f"Привіт, {name}! Як справи?"

# Виклик функції, який буде виконаний при запуску файлу
print(greet("Валерій"))
import requests
BASE_URL = "https://jsonplaceholder.typicode.com/posts" # <-- ВАЖЛИВО! Визначити тут
# 1. Створити словник (payload)
print("\n--- Task 2 ---")
post_payload = {
    'title': 'Мій перший пост',
    'body': 'Тестуємо POST-запити з Python!',
    'userId': 1
}
# 2. Зробити POST-запит
target_url = f"{BASE_URL}/posts"
response = requests.post(BASE_URL, json=post_payload)
# 3. Перевірити статус та вивести ID
if response.status_code == 201:
    print("Пост успішно створено!")
    data = response.json()
    print(f"ID нового поста: {data['id']}")
else:
    # Цей блок виконається, якщо код НЕ 201
    print(f"Щось пішло не так! Статус-код: {response.status_code}")
    print(f"Відповідь сервера: {response.text}") # .text покаже нам текст помилки