from django.test import TestCase
import requests

from .account_service import decode_token

# Create your tests here.

class AccountTest(TestCase):
    def setUp(self):
        self.email = "user123@user.com"
        self.password = "12345"
        self.username = "user" + "12345"
        self.nickname = "usernickname"

    
        self.signUpUrl = "http://localhost:8000/account/signup/"
        self.signUpData = {
            "username": self.username,
            "password": "12345",
            "email": self.email,
            "nickname": self.nickname,
            "select_baby": True,
            "account_open": True,
            "follower_open": True
        }

        self.loginUrl = "http://localhost:8000/account/login/"
        self.loginData = {
            "email": "qwe345@qwe.com",
            "password": self.password
        }

        self.perosnalUrl = "http://localhost:8000/account/" + self.nickname
        self.babyUrl = "http://localhost:8000/account/" + self.nickname + "/babies/"

        self.babyData = {
            "name": "baby2",
            "birthday": "2019-10-18",
            "spouse": "spouse1",
        }


    def Test_signup(self):
        result = requests.post(self.signUpUrl, self.signUpData)

        self.assertEqual(result.status_code, 201)
        

    def Test_login(self):
        result = requests.post(self.loginUrl, self.loginData)

        self.assertEqual(result.status_code, 200)
        

    def Test_decode_token(self):
        token = ""
        result = decode_token(token)

        self.assertEqual(result.status_code, 200)


    def Test_personal(self):
        result = requests.get(self.perosnalUrl)
        
        self.assertEqual(result.status_code, 200)


    def Test_baby(self):
        result = requests.get(self.babyUrl)
        
        self.assertEqual(result.status_code, 200)

    def Test_set_baby(self):
        result = requests.post(self.babyUrl, self.babyData)

        self.assertEqual(result.status_code, 201)

    def test_all(self):
        self.Test_signup()
        self.Test_set_baby()
        self.Test_login()
        self.Test_personal()
        self.Test_baby()