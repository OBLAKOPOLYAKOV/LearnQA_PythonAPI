"""
Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете
запрос.
Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр
method должен равняться ‘POST’.  И так далее.

Надо написать скрипт, который делает следующее:

1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

Не забывайте, что для GET-запроса данные надо передавать через params=
А для всех остальных через data=
Итогом должна быть ссылка на коммит со скриптом и ответы на все 4 вопроса.
"""

# Ответ:
"""https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/9753c21b1d502cac790acf1a6bfb0de3487c93bb
"""

import requests
from requests import request

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

#1.Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
resoult = requests.put(url)

print(f"1) URL: {url} после запроса без параметра method возвращает: '{resoult.text}', со статус кодом '"
      f"{resoult.status_code}'")

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
resoult2 = requests.head(url, data='HEAD')
if resoult2.text == '':
    a = 'НИЧЕГО НЕ ВЕРНУЛ'
    print(f"2) URL: {url} после запроса не из cписка с аналогичным запросу параметром method {a}, со статус кодом: {resoult2.status_code}'")
else:
    a = resoult2.text
    print(f"3) URL: {url} после запроса не из cписка с аналогичным запросу параметром method возвращает: '{resoult2.text}', со статус кодом '"
          f"{resoult2.status_code}'")

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

resoult3 = requests.get(url, params='GET')

print(f"3) URL: {url} после запроса c правильным method возвращает: '{resoult3.text}', со статус кодом '"
      f"{resoult3.status_code}'")

"""#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
И так для всех типов запроса.
Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
"""

methods = ['POST', 'GET', 'PUT', 'DELETE']

for method in methods:
    response = requests.get(url, params = method)
    if method != 'GET' and response.status_code == 200 or method == 'GET' and response.status_code != 200:
        print(f"Для метода GET и параметра {method} возвращается status code: {response.status_code} - так быть не должно")

    response = requests.post(url, data=method)
    if method != 'POST' and response.status_code == 200 or method == 'POST' and response.status_code != 200:
        print(
            f"Для метода POST и параметра {method} возвращается status code: {response.status_code} - хоть и не должен был")

    response = requests.put(url, data=method)
    if method != 'PUT' and response.status_code == 200 or method == 'PUT' and response.status_code != 200:
        print(
            f"Для метода PUT и параметра {method} возвращается status code: {response.status_code}- хоть и не должен был")

    response = requests.get(url, data=method)
    if method != 'DELETE' and response.status_code == 200 or method == 'DELETE' and response.status_code != 200:
        print(
            f"Для метода DELETE и параметра {method} возвращается status code: {response.status_code}, - так быть не должно")

methods = ['POST', 'GET', 'PUT', 'DELETE']
for type in methods:
    for params in methods:
        if type == 'GET':
            resoult4 = request(type, url, params=params)
        else:
            resoult4 = request(type, url, data=params)
        if type != params and resoult4.status_code == 200:
            print(f"method {type}, параметр {params} возвращает: '{resoult4.text}', со статус кодом '"
                f"{resoult4.status_code}'")
        elif type == params and resoult4.status_code != 200:
            print(f"method {type}, параметр {params} возвращает: '{resoult4.text}', со статус кодом '"
                  f"{resoult4.status_code}' - так быть не должно")