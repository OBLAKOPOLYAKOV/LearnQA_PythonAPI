import requests
import pytest

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
