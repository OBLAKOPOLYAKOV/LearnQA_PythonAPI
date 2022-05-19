import requests
import pytest


class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        length = 15
        assert len(phrase) < length,  f"Фраза длиннее 15 символов"