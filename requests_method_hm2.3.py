import json
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

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса.
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

#Способ 1:
methods = ['POST', 'GET', 'PUT', 'DELETE']

for method in methods:
    response = requests.get(url, params = method)
    if method != 'GET' and response.status_code == 200:
        print(f"Для метода GET и параметра {method} возвращается status code: {response.status_code}, хоть и не должен был")
    else:
        print(f"!!!Для метода GET c параметром {method} возвращается {response.status_code} ")
    response = requests.post(url, data=method)
    if method != 'POST' and response.status_code == 200:
        print(
            f"Для метода POST и параметра {method} возвращается status code: {response.status_code}, хоть и не должен был")
    else:
        print(f"!!!Для метода POST c параметром {method} возвращается {response.status_code} ")
    response = requests.put(url, data=method)
    if method != 'PUT' and response.status_code == 200:
        print(
            f"Для метода PUT и параметра {method} возвращается status code: {response.status_code}, хоть и не должен был")
    else:
        print(f"!!!Для метода PUT c параметром {method} возвращается {response.status_code} ")
    response = requests.get(url, data=method)
    if method != 'DELETE' and response.status_code == 200:
        print(
            f"Для метода DELETE и параметра {method} возвращается status code: {response.status_code}, хоть и не должен был")
    else:
        print(f"!!!Для метода DELETE c параметром {method} возвращается {response.status_code} ")


methods = ['POST', 'GET', 'PUT', 'DELETE']
for type in methods:
    for params in methods:
        if type == 'GET':
            resoult4 = request(type, url, params=params)
        else:
            resoult4 = request(type, url, data=params)
        if type == params and resoult4.status_code == 200:
            print(f"method {type}, параметр {params} возвращает: '{resoult4.text}', со статус кодом '"
                f"{resoult4.status_code}'")
        elif resoult4.status_code == 200:
            print(f"method {type}, параметр {params} возвращает: '{resoult4.text}', со статус кодом '"
                  f"{resoult4.status_code}' - хоть и не должен был")
        else:
            print(f"method {type}, параметр {params} возвращает: '{resoult4.text}', со статус кодом '"
                  f"{resoult4.status_code}' - как сюда попасть хз")

