from django.test import TestCase
from account.tests import AccountTest
import requests

# Create your tests here.
class DiaryTest(TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000/"
        self.postUrl = self.base_url + "diary/"

        self.post_body = {
            "title": "title1",
            "content": "content1",
            "token": ""
        }

        self.diary_id = "7"

        self.imageUrl = self.base_url + "diary/" + self.diary_id + "/images/"
        self.imageData = {
            'image': './testing1.gif'
        }

        self.user_name = "summoner123"
        self.user_diary_url = self.base_url + "diary/" + self.user_name + "/" 

        self.diary_url = self.base_url + "diary/" + self.diary_id + "/"

        self.put_body = {
            "title": "title2",
            "content": "content2",
            "token": ""
        }

        self.delete_body = {
            "token": ""
        }

        account_test = AccountTest()
        account_test.setUp()
        result = account_test.Test_login()
        
        token = result.json()
        self.post_body['token'] = token['token']
        self.put_body['token'] = token['token']
        self.delete_body['token'] = token['token']
    

    def Test_post(self):
        for i in range(10):
            response = requests.post(self.postUrl, self.post_body)
        
        self.assertEqual(response.status_code, 201)


    def Test_set_image(self):
        response = requests.post(url=self.imageUrl, data=self.imageData)
        
        self.assertEqual(response.status_code, 201)


    def Test_get_iamge(self):
        response = requests.get(self.imageUrl)

        self.assertEqual(response.status_code, 200)


    def Test_get_user_diary(self):
        response = requests.get(self.user_diary_url)

        self.assertEqual(response.status_code, 200)

    def Test_get_diary(self):
        response = requests.get(self.diary_url)

        self.assertEqual(response.status_code, 200)
        

    def Test_put_diary(self):
        response = requests.put(self.diary_url, self.put_body)

        self.assertEqual(response.status_code, 202)


    def Test_delete_diary(self):
        response = requests.delete(url=self.diary_url, data=self.delete_body)

        self.assertEqual(response.status_code, 200)


    # def test_all(self):
    #     self.Test_post()
        # self.Test_set_image()
        # self.Test_get_iamge()
        # self.Test_get_user_diary()
        # self.Test_get_diary()
        # self.Test_put_diary()
        # self.Test_delete_diary()
