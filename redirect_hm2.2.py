import json
import requests
url = 'https://playground.learnqa.ru/api/long_redirect'

#Были проблемы на м1 без хэдерсов, на стэковерфлоу нашел такое решениею
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
#определяем количество редиректов
len = int(len(result.history))

#Для каждого редиректа выводим урл и порядковый номер редиректа
for a in range(len):
    print(f"{a+1} URL: {result.history[a].url}")

print(f"Всего редиректов было {len}")