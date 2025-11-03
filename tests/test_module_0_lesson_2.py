def greet(name):
    return f"Привіт, {name}! Як справи?"

# Виклик функції, який буде виконаний при запуску файлу
print(greet("Валерій"))
import requests
URL_POST = "https://jsonplaceholder.typicode.com/posts" # <-- ВАЖЛИВО! Визначити тут
# 1. Створити словник (payload)
post_payload = {
    'title': 'Мій перший пост',
    'body': 'Тестуємо POST-запити з Python!',
    'userId': 1
}
# 2. Зробити POST-запит
response = requests.post(URL_POST, json=post_payload)
# 3. Перевірити статус та вивести ID
if response.status_code == 201:
    new_post_data = response.json()
    print("\n--- Результат POST-запиту ---")
    print("Пост успішно створено!")
    print(f"Отриманий ID нового посту: {new_post_data['id']}")
else:
    print(f"Помилка створення посту. Статус-код: {response.status_code}")
# Примітка: jsonplaceholder зазвичай повертає ID=101 для нових постів.