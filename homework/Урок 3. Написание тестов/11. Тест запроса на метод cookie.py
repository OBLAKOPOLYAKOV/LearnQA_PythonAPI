"""Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
=================================================
Результатом должна быть ссылка на коммит с тестом.
"""

# Ответ:
""" 
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/fca6b51228a6684494d26680977f9a7f5b60a73a
python -m pytest -s homework/test_cookie_hm3_2.py
"""


import requests


class TestCookie:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookies = response.cookies
        assert cookies is not None, f"cookies is null"
        print(cookies, '\n', cookies.get_dict())

        cookie_name = 'HomeWork'
        cookie_value = response.cookies.get('HomeWork')
        assert cookie_name in cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        print(cookie_value)