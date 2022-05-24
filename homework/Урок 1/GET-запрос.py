"""
В проекте создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
Затем с помощью функции print вывести содержимое текста в ответе на запрос. Когда скрипт будет готов -
давайте его закоммитим в наш репозиторий.
Результатом должна быть ссылка на коммит.
"""

# Ответ:
"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/d7a4f0f57b6d4f68576c433c3bdb8326e825b773
"""

import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
