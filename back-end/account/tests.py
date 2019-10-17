from django.test import TestCase
import requests

# Create your tests here.

class AccountTest(TestCase):
    def setUp(self):
        self.signUpUrl = "http://localhost:8000/account/signup/"
        self.signUpData = {
            "username": "test12",
            "password": "12345",
            "email": "qwe123@qwe.com",
            "nickname": "testing123",
            "select_baby": True,
            "account_open": True,
            "follower_open": True
        }

    def test_signup(self):
        result = requests.post(self.signUpUrl, self.signUpData)