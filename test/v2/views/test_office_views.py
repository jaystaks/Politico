import json

from unittest import TestCase


class OfficeViewTest(TestCase):
    def test_office_creation(self):
        """
        Tests Office Created Successfully
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "type": "State",
            "name": "Office of the President"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 201, "Office Creation Successful")
        self.assertEqual('Office of the President', response.json['data'][0]['name'])

    def test_existing_office(self):
        """ Tests No office was Duplicated """
        data = {
            "type": "State",
            "name": "Office of the President"
        }
        self.client.post('api/v2/offices', data=json.dumps(data), headers=self.generate_token_admin())
        response = self.client.post('api/v2/offices', data=json.dumps(data), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 409, "Office Already Exists")
        self.assertEqual('Office Already Exists', response.json['error'])

    def test_created_office_with_invalid_data(self):
        """
        Tests Office with invalid data
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "name": "stat",
            "type": "prezzo"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400, "Should Parse Invalid Data ,Bad Request")
        self.assertIn('Check Input Values', response.json['error'])

    def test_create_office_with_missing_data(self):
        """
        Tests create office with missing data
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Governor"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400, "Should Parse Invalid Data ,Bad Request")
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])

    def test_get_all_offices_empty(self):
        """
        Tests that the offices in the db are retrieved as empty list if none
        """
        response = self.client.get('api/v2/offices', headers=self.generate_token())
        self.assertEqual(response.status_code, 200, "Should be getting all offices")
        self.assertEqual(0, len(response.json['data']))

    def test_get_all_offices_success(self):
        """
        Tests that all offices are retrieved
        """
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Senator",
            "type": "Local Government"
        }), headers=self.generate_token_admin())

        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Member of Parliament",
            "type": "Local government"
        }), headers=self.generate_token_admin())
        response = self.client.get('api/v2/offices', headers=self.generate_token())
        self.assertEqual(response.status_code, 200, "Should be getting all offices")
        self.assertEqual(2, len(response.json['data']))

    def test_office_edited_successfully(self):
        """"
        Tests that offices are edited successfully
        """
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Member of Parliament",
            "type": "Local government"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/offices/{}/name'.format(1), data=json.dumps({
            "name": "Office of the President"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated successfully', response.json['message'])

    def test_office_edited_unsuccessful_missing_key(self):
        response = self.client.patch('api/v2/offices/{}/name'.format(1), data=json.dumps({
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])

    def test_office_edited_exists(self):
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Governor",
            "type": "Local Government"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Governor",
            "type": "Local"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/offices/{}/name'.format(1), data=json.dumps({
            "name": "Governor"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 409)
        self.assertIn('Office with similar name exists', response.json['error'])

    def test_office_edited_data_invalid(self):
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Governor",
            "type": "Local"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/offices/{}/name'.format(1), data=json.dumps({
            "name": "Gov"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid Data ,Check id or data being updated', response.json['error'])

    def test_specific_office_success(self):
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Governor",
            "type": "Local Government"
        }), headers=self.generate_token_admin())
        response = self.client.get("api/v2/offices/1", headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Office of the Governor', response.json['data'][0]['office_name'])

    def test_get_non_existing_office(self):
        response = self.client.get("api/v2/offices/1", headers=self.generate_token())
        self.assertEqual(response.status_code, 404)
        self.assertIn('Office Not Found', response.json['error'])

    def test_get_office_with_invalid_id(self):
        response = self.client.get("api/v2/offices/---", headers=self.generate_token())
        self.assertEqual(response.status_code, 404)
        self.assertIn('Office Not Found', response.json['error'])

    def test_delete_office_success(self):
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Office of the Governor",
            "type": "Local Government"
        }), headers=self.generate_token_admin())
        response = self.client.delete("api/v2/offices/1", headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Office of the Governor Deleted', response.json['message'])

    def test_delete_office_fail(self):
        response = self.client.delete("api/v2/offices/1", headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('Office Not Found', response.json['error'])
