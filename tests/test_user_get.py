import requests
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import allure


@allure.epic("Get user info cases")
class TestUserGet(BaseCase):

    @allure.description("This test without login trying to get info details user")
    def test_get_user_details_not_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        Assertions.assert_json_has_key(response, "username")
        keys = [
            "email", "firstName", "lastName"
        ]
        Assertions.assert_json_has_not_keys(response, keys)

    @allure.description("This test login system and trying to get info details another user")
    def test_get_user_details_auth_as_another_user(self):
        # Login user with id=2:
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        keys = [
            "email", "firstName", "lastName"
        ]
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        # Create new user, and get user id:
        url = "/user/"
        data = self.prepare_registration_data()
        response2 = MyRequests.post(url, data=data)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        user_id_from_auth_method = self.get_json_value(response2, "id")

        # Get user from 'response2' details auth as id2 user:

        response3 = MyRequests.get(f"/user/{user_id_from_auth_method}", headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_keys(response3, keys)

    @allure.description("This test login system and trying to get user info with correct token")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}", headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)
