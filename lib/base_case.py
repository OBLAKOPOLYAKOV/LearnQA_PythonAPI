import json.decoder

from datetime import datetime
from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find headers with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON Format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON dosen`t have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None, name=None, name_args: int = 1, exclude_data=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S%f")
            email = f"{base_part}{random_part}@{domain}"

        if name is None:
            name = "learnqa"

        registration_data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': name * name_args,
            'lastName': 'learnqa',
            'email': email
        }

        if exclude_data is not None:
            for data in registration_data:
                if data == exclude_data:
                    registration_data[data] = ''

        return registration_data
