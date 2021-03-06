import os


class Enviroment:
    DEV='dev'
    PROD='prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/api_dev',
        PROD: 'https://playground.learnqa.ru/api'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except  KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(F"unknown value of ENV varieble {self.env}")


ENV_OBJECT = Enviroment()
