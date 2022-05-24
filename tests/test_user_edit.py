import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from datetime import datetime


class TestUserEdit(BaseCase):
    exclude_critical_data = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]

    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Change Name"
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})
        Assertions.asser_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    @pytest.mark.parametrize('exclude_data', exclude_critical_data)
    def test_edit_user_without_login(self, exclude_data):
        # REGISTER: Create new user.
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")
        data = register_data[exclude_data]
        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }
        if exclude_data == 'email':
            new_data = datetime.now().strftime("%m%d%Y%H%M%S%f") + '@newmail.com'
        else:
            new_data = "Change something"

        # EDIT: change firstname without login.
        response2 = MyRequests.put(f"/user/{user_id}", data={exclude_data: new_data})
        Assertions.assert_code_status(response2, 400)

        # LOGIN: logging with a new user's data from 1 step
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET: Get user data with auth. Check that the name has not changed
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})
        Assertions.asser_json_value_by_name(response4, exclude_data, data, "Wrong data of the user after edit without "
                                                                           "login !")

    @pytest.mark.parametrize('exclude_data', exclude_critical_data)
    def test_change_data_with_login_other_user(self, exclude_data):
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

        # EDIT: edit 2 user with sid and token by 1 user.
        if exclude_data == 'email':
            new_data = datetime.now().strftime("%m%d%Y%H%M%S%f") + '@newmail.com'
        else:
            new_data = "Change something"
        response4 = MyRequests.put(f"/user/{user_id2}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={exclude_data: new_data})
        Assertions.assert_code_status(response4, 200)

        # LOGIN: logging with a 2nd user's data from 2 step
        email2 = register_data2['email']
        password2 = register_data2['password']
        login_data2 = {
            'email': email2,
            'password': password2
        }
        response5 = MyRequests.post("/user/login", data=login_data2)
        auth_sid2 = self.get_cookie(response5, "auth_sid")
        token2 = self.get_header(response5, "x-csrf-token")

        # GET: Get firstname user data with auth. Check that the name has not changed
        data = register_data2[exclude_data]
        response6 = MyRequests.get(f"/user/{user_id2}",
                                   headers={"x-csrf-token": token2},
                                   cookies={"auth_sid": auth_sid2}
                                   )
        Assertions.asser_json_value_by_name(response6, exclude_data, data, "Wrong name of the user after edit without "
                                                                           "login !")

    def test_change_different_email(self):
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

        # EDIT: Change email on different email
        new_email = 'defferentemail.com'
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={'email': new_email})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text(response3, "Invalid email format")

    def test_change_firstname_to_different_value(self):
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

        # EDIT: Change email on different email
        new_name = 'a'
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={'firstName': new_name})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text(response3, "Too short value for field firstName")