import json
from unittest import TestCase

from app import politico
from app.api.db.database import init_app


class TestOffice(TestCase):
    def setUp(self):
        self.app = politico("testing")
        self.client = self.app.test_client()
        self.officeID = 6
        self.endpoint = "/api/v2/offices"
        self.data = {
            "type": "Legislative",
            "name": "Office Name 1"
        }
        self.dataNoNameProperty = {
            "type": "Legislative",
        }
        self.dataEmptyValues = {
            "type": "",
            "name": ""
        }
        self.dataRegisterCandidate = {
            "candidate": 6,
            "office": 2,
            "party": 2
        }
        self.dataUpdate = {
            "type": "Legislative",
            "name": "Updated"
        }
        self.data = {
            "email": "admin@gmail.com",
            "password": "adminpass"
        }

    def tearDown(self):
        init_app()

    def loginUser(self):
        response = self.client.post(path="/api/v2/auth/login",
                                    data=json.dumps(self.data),
                                    content_type='application/json')
        token = response.json["data"]["token"]
        return {
            "Authorization": "Bearer " + token
        }

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data),
                                content_type='application/json',
                                headers=self.loginUser())

    def get(self, path):
        return self.client.get(path=path, content_type='application/json', headers=self.loginUser())

    def patch(self, path, data):
        return self.client.patch(path=path, data=json.dumps(data),
                                 content_type='application/json',
                                 headers=self.loginUser())

    def delete(self, path):
        return self.client.delete(path=path, content_type='application/json', headers=self.loginUser())

    def test_create_office(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_office(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_edit_specific_office(self):
        post_office = self.post(self.endpoint, self.data)
        response = self.patch(self.endpoint + "/" + str(self.officeID), self.dataUpdate)
        self.assertEqual(response.status_code, 200)

    def test_edit_specific_office_not_found(self):
        response = self.patch(self.endpoint + "/2000", self.dataUpdate)
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_office(self):
        post_office = self.post(self.endpoint, self.data)
        response = self.delete(self.endpoint + "/" + str(self.officeID))
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_office_not_found(self):
        response = self.delete(self.endpoint + "/2000")
        self.assertEqual(response.status_code, 404)

    def test_get_specific_office(self):
        post_office = self.post(self.endpoint, self.data)
        response = self.get(self.endpoint + "/" + str(self.officeID))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_office_not_found(self):
        response = self.get(self.endpoint + "/2000")
        self.assertEqual(response.status_code, 404)

    def test_register_candidate_to_office(self):
        response = self.post(self.endpoint + "/register", self.dataRegisterCandidate)
        self.assertEqual(response.status_code, 200)

    def test_specific_office_results(self):
        response = self.get(self.endpoint + "/1/result")
        self.assertEqual(response.status_code, 200)

    def test_specific_office_results_not_found(self):
        response = self.get(self.endpoint + "/2000/result")
        self.assertEqual(response.status_code, 404)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmptyValues)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoNameProperty)
        self.assertEqual(response.status_code, 400)
