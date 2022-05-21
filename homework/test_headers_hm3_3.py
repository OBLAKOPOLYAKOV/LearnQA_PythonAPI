import requests


class TestHeaders:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.post(url)

        headers = response.headers
        print(headers)
        assert headers is not None, f"headers is null"

        headers_name = 'x-secret-homework-header'
        print(headers[headers_name])
        assert headers_name in headers, f"Cannot find headers with name {headers_name} in the last response"