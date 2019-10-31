from django.test import TestCase
from account.tests import AccountTest
import requests, json

# Create your tests here.
class DiaryTest(TestCase):
    def setUp(self):
        account_test = AccountTest()
        account_test.setUp()
        account_test.Test_signup()
        result = account_test.Test_login()
        token = result.json()

        self.base_url = "http://localhost:8000/"
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}

        self.postUrl = self.base_url + "diary/"

        self.post_body = {
            "title": "title1",
            "content": "content1",
            "token": ""
        }

        self.user_name = account_test.nickname

        self.imageUrl = ""
        self.imageData = {
            'image': './testing1.gif',
            'token': ''
        }

        self.tokenData = {
            'token': ''
        }

        self.user_diary_url = self.base_url + "diary/" + self.user_name + "/" 

        self.diary_url = ""

        self.put_body = {
            "title": "title2",
            "content": "content2",
            "token": ""
        }

        self.delete_body = {
            "token": ""
        }
        
        self.post_body['token'] = token['token']
        self.put_body['token'] = token['token']
        self.imageData['token'] = token['token']
        self.tokenData['token'] = token['token']
        self.delete_body['token'] = token['token']
    

    def Test_post(self):
        response = requests.post(self.postUrl, data=json.dumps(self.post_body), headers=self.headers)
        
        self.assertEqual(response.status_code, 201)


    def Test_set_image(self):
        response = requests.post(url=self.imageUrl, data=json.dumps(self.imageData), headers=self.headers)
        
        self.assertEqual(response.status_code, 201)


    def Test_get_image(self):
        response = requests.get(self.imageUrl, data=json.dumps(self.tokenData), headers=self.headers)

        print(response.json())

        self.assertEqual(response.status_code, 200)


    def Test_get_user_diary(self):
        response = requests.get(self.user_diary_url, data=json.dumps(self.tokenData), headers=self.headers)

        print(response.json())

        self.diary_id = response.json()[0].get('id')

        self.imageUrl = self.base_url + "diary/" + str(self.diary_id) + "/images/"
        self.diary_url = self.base_url + "diary/" + str(self.diary_id) + "/"

        self.assertEqual(response.status_code, 200)


    def Test_get_diary(self):
        response = requests.get(self.diary_url, data=json.dumps(self.tokenData), headers=self.headers)

        print(response.json())

        self.assertEqual(response.status_code, 200)
        

    def Test_put_diary(self):
        response = requests.put(self.diary_url, data=json.dumps(self.put_body), headers=self.headers)

        self.assertEqual(response.status_code, 202)


    def Test_delete_diary(self):
        response = requests.delete(url=self.diary_url, data=json.dumps(self.delete_body), headers=self.headers)

        self.assertEqual(response.status_code, 200)


    def test_all(self):
        self.Test_post()
        self.Test_get_user_diary()
        # self.Test_set_image()
        # self.Test_get_image()
        self.Test_get_diary()
        self.Test_put_diary()
        self.Test_delete_diary()
