"""
В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу
короче 15 символов. А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
phrase = input("Set a phrase: ")
Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком
"-s": python -m pytest -s my_test.py
=========================================
Результатом должна стать ссылка на такой тест.

"""

# Ответ:

"""
https://github.com/OBLAKOPOLYAKOV/LearnQA_PythonAPI/commit/97a035eb736132d2301e8d80c319f55d0a42b10e
python -m pytest -s homework/test_phrase_hm3_1.py
"""

import requests
import pytest


class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        length = 15
        assert len(phrase) < length,  f"Фраза длиннее 15 символов"