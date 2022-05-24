import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import pytest


class TestUserRegister(BaseCase):
    exclude_critical_data = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]

    def test_create_user_successfully(self):
        url = "/user/"
        data = self.prepare_registration_data()

        response = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        url = "/user/"
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        url = "/user/"
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text(response, f"Invalid email format")

    def test_create_user_with_one_symbol_name(self):
        url = "/user/"
        name = "a"
        data = self.prepare_registration_data(name=name)
        response = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text(response, f"The value of 'firstName' field is too short")

    def test_create_user_with_250_symbol_name(self):
        url = "/user/"
        name = "a"
        data = self.prepare_registration_data(name=name, name_args=250)
        response = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @pytest.mark.parametrize('exclude_data', exclude_critical_data)
    def test_create_user_with_out_critical_data(self, exclude_data):
        url = "/user/"
        data = self.prepare_registration_data(exclude_data=exclude_data)
        response = MyRequests.post(url, data=data)
        Assertions.assert_response_text(response, f"The value of '{exclude_data}' field is too short")
        Assertions.assert_code_status(response, 400)
