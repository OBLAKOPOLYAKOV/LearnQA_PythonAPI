"""
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers
и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
=============================================================
Результатом должна быть ссылка на коммит с тестом.
"""
# Ответ:
"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/54d756e86734b1537936d2dce9499358b30932b7
python -m pytest -s homework/test_headers_hm3_3.py
"""

import requests


class TestHeaders:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.post(url)

        headers = response.headers
        print(headers)
        assert headers is not None, f"headers is null"

        headers_name = 'x-secret-homework-header'
        print(headers[headers_name])
        assert headers_name in headers, f"Cannot find headers with name {headers_name} in the last response"