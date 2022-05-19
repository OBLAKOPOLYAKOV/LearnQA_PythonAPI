import requests
import time

#1. Создаем задачу
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

