from django.test import TestCase
import requests

# Create your tests here.

class AccountTest(TestCase):
    email = "qwe123@qwe.com"
    password = "12345"
    username = "test" + "123"

    def setUp(self):
        self.signUpUrl = "http://localhost:8000/account/signup/"
        self.signUpData = {
            "username": username,
            "password": "12345",
            "email": email,
            "nickname": "testing123",
            "select_baby": True,
            "account_open": True,
            "follower_open": True
        }

        self.loginUrl = "http://localhost:8000/account/login/"
        self.loginData = {
            "email": "qwe345@qwe.com",
            "password": password
        }


    def test_signup(self):
        result = requests.post(self.signUpUrl, self.signUpData)

        self.assertEqual(result.status_code, 201)
        

    def test_login(self):
        result = requests.post(self.loginUrl, self.loginData)

        self.assertEqual(result.status_code, 200)
        
        
