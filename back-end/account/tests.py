from django.test import TestCase
import requests

# from .account_service import decode_token
import jwt

# Create your tests here.

class AccountTest(TestCase):
    
    def setUp(self):
        self.email = "qwe123@qwe.com"
        self.password = "12345"
        self.username = "test" + "123"

    
        self.signUpUrl = "http://localhost:8000/account/signup/"
        self.signUpData = {
            "username": self.username,
            "password": "12345",
            "email": self.email,
            "nickname": "testing123",
            "select_baby": True,
            "account_open": True,
            "follower_open": True
        }

        self.loginUrl = "http://localhost:8000/account/login/"
        self.loginData = {
            "email": "qwe123@qwe.com",
            "password": self.password
        }

        self.logoutUrl = "http://localhost:8000/account/logout/"
        self.logoutData = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImdoZGNqZjkwMzlAZ21haWwuY29tIiwiZXhwIjoiMjAxOS0xMC0yMSAwNjoxNTowOS42NTE5MTkifQ.Y-f_ciy7N2O_udH2jfN-B4dM1PSK9Bp7LfOdwQyHYQc"
        }


    def Test_signup(self):
        result = requests.post(self.signUpUrl, self.signUpData)

        self.assertEqual(result.status_code, 201)
        

    def test_login(self):
        result = requests.post(self.loginUrl, self.loginData)

        self.assertEqual(result.status_code, 200)
        
    def Test_logout(self):
        result = requests.post(self.logoutUrl, self.logoutData)

        self.assertEqual(result.status_code, 200)

    def test_all(self):
        self.Test_signup()
        self.Test_login()
