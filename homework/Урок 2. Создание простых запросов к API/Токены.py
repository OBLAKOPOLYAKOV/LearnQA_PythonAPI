"""Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить
готовый ответ. Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию
по разным источникам.

В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще
не готова, ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.

Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job

Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со
следующими полями:

* seconds - количество секунд, через сколько задача будет выполнена
* token - тот самый токен, по которому можно получить результат выполнения нашей задачи

Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:

* error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе
будет следующая надпись - No job linked to this token
* status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
* result - будет только в случае, если задача готова, это поле будет содержать результат

Наша задача - написать скрипт, который делал бы следующее:

1) создавал задачу
2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
"""

# Ответ:

"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/5797182f340b68811a147cc8c57d745a5e2c438d
"""

import requests
import time

# 1. Создаем задачу

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
tokenkey = "token"
timekey = "seconds"
exstatus= 'Job is NOT ready'
exresult = 'Job is ready'
exerror = 'No job linked to this token'
condition = {'status': 'status',
             'error': 'error',
             'result': 'result'}

print(f"получаем токен:")
response4token = requests.get(url)
obj = response4token.json()
token = obj['token']
params = {'token': token}
timetosleep = obj[timekey]
print(f"token:{token}, time: {timetosleep}")

#2. Делаем запрос до истечения времению
print(f"Делаем запрос до выполнения задания")
responsebeforeready = requests.get(url, params=params)
conditionobj = responsebeforeready.json()
if condition['error'] in conditionobj:
    print(f"Запрос вернул ошибку")
elif condition['result'] in conditionobj:
    print(f"Задача еще не готова: {conditionobj[condition['result']]}")
    assert exresult == conditionobj[condition['result']], 'Status text не соответствует требованиям'
else:
    print(f"Задача еще не готова: {conditionobj[condition['status']]}")

#3 Ждем нужное количество секунд
print(f"Ждем {timetosleep} секунд")
time.sleep(timetosleep+2)

#4 Делаем запрос с токен, после того как задача готова:
print(f"Делаем запрос, после того как нужное время прошло")
responsebeforeready = requests.get(url, params=params)
conditionobj = responsebeforeready.json()
if condition['error'] in conditionobj:
    print(f"Запрос вернул ошибку")
elif condition['result'] in conditionobj:
    print(f"Задача готова: {conditionobj[condition['result']]}")
    assert exresult == conditionobj[condition['status']], 'Status text не соответствует требованиям'
else:
    print(f"Задача еще не готова: {conditionobj[condition['status']]}")
