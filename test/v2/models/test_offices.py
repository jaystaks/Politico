import json
from unittest import TestCase

from app import politico
from app.api.v2.utils.tester import create_office2, office_keys, office_name, category_restriction


class TestOffice(TestCase):

    def setUp(self):
        self.client = politico("testing").test_client()

    def test_wrong_category_value(self):
        """
        Test create a new office.
        """

        response = self.client.post(
            '/api/v2/offices', data=json.dumps(category_restriction), content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'select from state, local, federal or legislative')
        assert response.status_code == 400

    def test_unexisting_officeUrl(self):
        """
        Test wrong url.
        """

        response = self.client.get(
            '/api/v2/office')
        result = json.loads(response.data.decode())
        assert response.status_code == 404
        assert result['status'] == "not found"

    def test_office_keys(self):
        """
        Test office json keys
        """

        response = self.client.post(
            '/api/v2/offices', data=json.dumps(office_keys), content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid category key')
        assert response.status_code == 400

    def test_get_offices(self):
        """
        Test fetching all offices.
        """

        response = self.client.get(
            '/api/v2/offices', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "success")
        assert response.status_code == 200

    def test_unexisting_offices(self):
        """
        Test fetching all offices.
        """

        response = self.client.get(
            '/api/v2/offices', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], "success")
        assert response.status_code == 200

    def test_get_office(self):
        """
        Test getting a specific office by id.
        """

        response1 = self.client.post(
            '/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
        return response1
        response = self.client.get(
            '/api/v2/offices/1', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'success')
        assert response.status_code == 200

    def test_unexisting_office(self):
        """
        Test fetching unexisting office.
        """

        response = self.client.get(
            '/api/v2/offices/500', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        assert response.status_code == 404
        assert result['status'] == "not found"

    def test_office_nameValue(self):
        """
        Test name json values.
        """

        response = self.client.post(
            '/api/v2/offices', data=json.dumps(office_name), content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'The name of the office is in wrong format!')
        assert response.status_code == 400

    def test_delete_office(self):
        """
        Test deleting a specific office by id.
        """

        response1 = self.client.post(
            '/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
        response = self.client.delete(
            '/api/v2/offices/1/delete', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'office deleted')
        assert response.status_code == 200