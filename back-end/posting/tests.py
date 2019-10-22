from django.test import TestCase
from account.tests import AccountTest
import requests

# Create your tests here.
class DiaryTest(TestCase):
    def setUp(self):
        self.postUrl = "http://localhost:8000/diary/"

        self.post_body = {
            "title": "title1",
            "content": "content1",
            "token": ""
        }

        self.loginUrl = "http://localhost:8000/account/login/"
        self.loginData = {
            "email": "user987@user.com",
            "password": "12345"
        }
    

    def Test_login(self):
        result = requests.post(self.loginUrl, self.loginData)

        self.assertEqual(result.status_code, 200)
        
        return result

    def test_post(self):
        result = self.Test_login()
        token = result.json()
        self.post_body['token'] = token['token']

        response = requests.post(self.postUrl, self.post_body)
        print(response)