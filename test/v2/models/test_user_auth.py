import json

from unittest import TestCase
from app import politico


class TestAuth(TestCase):
    def setUp(self):
        self.app = politico("testing").test_client()
        self.endpoint = "/api/v2/auth"
        self.user_data = {
          "firstname": "Bob",
          "lastname": "Is",
          "othername": "Name",
          "email": "someemail@me.com",
          "phoneNumber": "0799999999",
          "passportUrl": "https://someurl.com",
          "password": "zaqxswcde123",
          "isAdmin": False
        }

    def test_signup(self):
        """
        Test that Users can Signup
        """
        response = self.app.post(
            self.endpoint + '/signup',
            data=self.user_data
        )

        self.assertEqual(response.status_code, 201)

    def test_login(self):
        """
        Test that Registerd Users can login
        """
        response = self.app.post(
            self.endpoint + '/signup',
            data=self.user_data
        )

        self.assertEqual(response.status_code, 201)

        response = self.app.post(
            self.endpoint + '/login',
            data={
                "email": self.user_data["email"],
                "password": self.user_data["password"]
            }
        )

        self.assertEqual(response.status_code, 200)


    def test_already_registered_user(self):
        """
        Test registration with an already registered email
        """
        response = self.app.post(
            self.endpoint + '/login',
            data={
                "email": self.user_data["email"],
                "password": self.user_data["password"]
                }
            )
        data = json.loads(response.user_data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(
            data['message'] == 'User already exists. Please Log in.')
        self.assertEqual(response.status_code, 202)

    def test_no_user_login(self):
        """
        Test for login of non-registered user
        """
        response = self.app.post(
            self.endpoint + '/login',
            data={
                "email": self.user_data["email"],
                "password": self.user_data["password"]
            }
        )
        data = json.loads(response.user_data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(data['message'] == 'User does not exist.')
        self.assertEqual(response.status_code, 404)

    def test_signup_empty_values(self):
        response = self.post(
        self.endpoint + "/signup",
        data = {
          "firstname": "",
          "lastname": "",
          "othername": "",
          "email": "",
          "phoneNumber": "",
          "passportUrl": "",
          "password": "",
          "isAdmin": False
        })
        self.assertEqual(response.status_code, 422)

    def test_login_empty_values(self):
        response = self.post(self.endpoint + "/login",
        data={
            "email": self.user_data[""],
            "password": self.user_data[""]
        })
        self.assertEqual(response.status_code, 422)
