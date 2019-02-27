import json
from unittest import TestCase

import self as self

from app.api.v2.utils.tester import create_account, email_value, phone_value, user_login, unregistered_user, \
    email_exists, phone_exists


class TestUsersAccount(TestCase):

    def test_token(self):
        self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
                         content_type='application/json')

    response = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
                                content_type='application/json')
    access_token = json.loads(response.get_data(as_text=True))['token']
    auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
    # return auth_header


def test_email_exists(self):
    response = self.client.post(
        '/api/v2/auth/signup', data=json.dumps(email_exists), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'Email already exists!')
    assert response.status_code == 400


def test_phone_number(self):
    response = self.client.post(
        '/api/v2/auth/signup', data=json.dumps(phone_exists), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'Phone number already exists!')
    assert response.status_code == 400


def test_signin(self):
    response = self.client.post(
        '/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'successfully logged in user@admin.co.ke', msg='not allowed')
    assert response.status_code == 200


def test_unexisting_url(self):
    response = self.client.post(
        '/api/v2/auth/loggin', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['status'], 'not found', msg='not found')
    assert response.status_code == 404


def test_unexisting_user(self):
    response = self.client.post(
        '/api/v2/auth/login', data=json.dumps(unregistered_user), content_type='application/json',
        headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'Invalid credentials', msg='not allowed')
    assert response.status_code == 401


def test_email_format(self):
    response = self.client.post(
        '/api/v2/auth/signup', data=json.dumps(email_value), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'Email in wrong format')
    assert response.status_code == 400


def test_phonenumber_format(self):
    response = self.client.post(
        '/api/v2/auth/signup', data=json.dumps(phone_value), content_type='application/json', headers=self.get_token())
    result = json.loads(response.data.decode())
    self.assertEqual(result['message'], 'wrong phone format')
    assert response.status_code == 400
