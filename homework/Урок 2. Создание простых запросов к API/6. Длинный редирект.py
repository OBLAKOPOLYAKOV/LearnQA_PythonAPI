"""
Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки
назначения до итоговой. И какой URL итоговый.
Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL.
"""

# Ответ:

"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/a0a6d1f63b94a14d7c6e9d62050212357725ade8

URL: https://learnqa.ru/ - Последний!
Всего редиректов было 3

"""

import requests

url = 'https://playground.learnqa.ru/api/long_redirect'

# Были проблемы на м1 без хэдерсов, на стэковерфлоу нашел такое решениею
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
# определяем количество редиректов
len = int(len(result.history))

# Для каждого редиректа выводим урл и порядковый номер редиректа
for a in range(len):
    if a + 1 == len:
        print(f"{a + 1} URL: {result.history[a].url} - Последний!")
    else:
        print(f"{a + 1} URL: {result.history[a].url}")
print(f"Всего редиректов было {len}")