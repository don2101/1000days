from django.test import TestCase
import requests

import jwt

# Create your tests here.

class AccountTest(TestCase):
    def setUp(self):
        self.base_url = "http://13.124.234.2:8000/"

        self.email = "setpwuser@gmail.com"
        self.password = "12345"
        self.username = "setpw"
        self.nickname = "setpw"

    
        self.signUpUrl = self.base_url + "account/signup/"
        self.signUpData = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "introduce": "introducing me",
            "nickname": self.nickname,
            "select_baby": True,
            "account_open": True,
            "follower_open": True
        }

        self.loginUrl = self.base_url + "account/login/"
        self.loginData = {
            "email": self.email,
            "password": self.password
        }

        self.perosnalUrl = self.base_url + "account/" + self.nickname
        self.babyUrl = self.base_url + "account/" + self.nickname + "/babies/"

        self.babyData = {
            "name": "park's baby",
            "birthday": "2019-10-23",
            "spouse": "park's spouse",
        }
        
        self.followUrl = self.base_url + "account/" + self.nickname + "/follow/"
        self.followData = {
            "follow": "summoner123"
        }
        self.logoutUrl = self.base_url + "account/logout/"
        self.logoutData = {
            "token": ""
        }


    def Test_signup(self):
        result = requests.post(self.signUpUrl, self.signUpData)

        self.assertEqual(result.status_code, 201)
        

    def Test_login(self):
        result = requests.post(self.loginUrl, self.loginData)

        self.assertEqual(result.status_code, 200)
        
        return result

    def Test_decode_token(self):
        token = ""
        result = decode_token(token)

        self.assertEqual(result.status_code, 200)


    def Test_logout(self):
        result = requests.post(self.logoutUrl, self.logoutData)

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

    def Test_follow(self):
        result = requests.post(self.followUrl, self.followData)

        self.assertEqual(result.status_code, 200)

    # def test_all(self):
    #     self.Test_signup()
    #     self.Test_set_baby()
    #     self.Test_login()
    #     self.Test_personal()
    #     self.Test_baby()
    #     self.Test_follow()
        # self.Test_logout()

    # def test_login_and_logout(self):
    #     response = self.Test_login()

    #     self.assertEqual(response.status_code, 200)

    #     self.logoutData['token'] = response.json()['token']
    #     self.Test_logout()

    #     self.assertEqual(response.status_code, 200)



