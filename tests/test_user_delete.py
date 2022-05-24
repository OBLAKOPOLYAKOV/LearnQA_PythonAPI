import allure
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("Delete cases")
class TestUserDelete(BaseCase):
    @allure.description("Попытка удаления Админ. пользователя")
    def test_delete_admin_user(self):
        # LOGIN: login with admin data
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        # Delete admin user.
        response2 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text(response2, "Please, do not delete test users with ID 1, 2, 3, 4 or 5")

    @allure.description("This test delete user from system")
    def test_delete_user(self):
        # REGISTER: Create new user 1.
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        # LOGIN: logging with a first user's data from 1 step
        email = register_data['email']
        password = register_data['password']
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response1, "id")

        # DELETE: DELETE USER
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3, 200)

        # GET: Get firstname user data with auth. Check that the name has not changed
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_response_text(response4, "User not found")

    @allure.description("This test trying delete other user from system")
    def test_delete_other_user(self):
        # REGISTER: Create new user 1.
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        # LOGIN: logging with a first user's data from 1 step
        email = register_data1['email']
        password = register_data1['password']

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # REGISTER: Create new user 2
        register_data2 = self.prepare_registration_data()
        response3 = MyRequests.post("/user/", data=register_data2)
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")
        user_id2 = self.get_json_value(response3, "id")

        # Delete: Delete second user with token by first user
        response4 = MyRequests.delete(f"/user/{user_id2}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3, 200)
        print(response4.text)

        # LOGIN: logging with a 2nd user's data from 2 step
        email2 = register_data2['email']
        password2 = register_data2['password']
        login_data2 = {
            'email': email2,
            'password': password2
        }
        response5 = MyRequests.post("/user/login", data=login_data2)
        Assertions.assert_json_has_key(response5, "user_id")
        Assertions.asser_json_value_by_name(response5, 'user_id', user_id2, f"after delete method user id was changed")
