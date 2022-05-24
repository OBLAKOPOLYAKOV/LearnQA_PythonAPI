"""
Давайте создадим пустой Python-скрипт.
Внутри него создадим переменную json_text. Значение этой переменной должно быть таким, как указано тут:
https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37
Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text
и вывести текст второго сообщения с помощью функции print.
Ответом должна быть ссылка на скрипт в вашем репозитории.
"""

# Ответ:
"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/ad3b95dad984496f36762e1567b3a5fea299a912

"""
import json


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
key = "messages"
key2 = "message"
#парсим все что внутри messages
obj = json.loads(json_text)
#выводим конкретный тег message
obj2 = obj[key][1]
print(obj2[key2])