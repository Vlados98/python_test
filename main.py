import requests
import json


class TestMySecondTest:
    def test_post_users(self):
        response_body = requests.request('post', 'https://reqres.in/api/users').json()
        print(response_body)


