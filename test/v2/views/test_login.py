import json
from unittest import TestCase

from app import politico
from app.api.db.database import init_app


class TestUsers(TestCase):
    def setUp(self):
        self.app = politico("testing")
        self.client = self.app.test_client()
        self.userID = 1
        self.data = {
            "email": "admin@example.com",
            "password": "pass123"
        }

    def tearDown(self):
        init_app()

    def loginUser(self):
        response = self.client.post("/api/v2/auth/login", data=json.dumps(self.data),
                                    content_type='application/json')
        token = response.json["token"]
        return {
            "Authorization": " Bearer " + token
        }

    def get(self):
        return self.client.get(content_type='application/json', headers=self.loginUser())

    def test_get_specific_user(self):
        response = self.get("/api/v2/user/" + str(self.userID))
        self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        response = self.get("/api/v2/user")
        self.assertEqual(response.status_code, 200)

    def test_get_specific_candidate_party(self):
        response = self.get("/api/v2/user/candidate/party/" + str(self.userID))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_candidate_office(self):
        response = self.get("/api/v2/user/candidate/office/" + str(self.userID))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_candidate_party_not_found(self):
        response = self.get("/api/v2/user/candidate/party/454545")
        self.assertEqual(response.status_code, 404)

    def test_get_specific_candidate_office_not_found(self):
        response = self.get("/api/v2/user/candidate/office/454545")
        self.assertEqual(response.status_code, 404)
