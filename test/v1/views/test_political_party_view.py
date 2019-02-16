"""
Tests for Political Party Views
"""
from instance.config import appConfig
from app import politico
from unittest import TestCase
from app.api.v1.models.political_model import Political


class TestPoliticalPartyViews(TestCase):
  """
  Test Political Party Views Class
  """
  def setUp(self):
      self.app = politico('testing').test_client()
      self.political_party = {
        "name": "Sample Ultiman",
        "hqAddress": "Some Address",
        "logoUrl": "example.com"}

  def test_get_political_party(self):
    """
    Test Political Parties get
    """
    Political().create_political_party(
      "Sample Get", "Some Address", "example.com")
    response = self.app.get('/api/v1/parties')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample Get', str(response.data))

  def test_create_political_parties(self):
    """
    Test Political Parties create
    """
    response = self.app.post(
      '/api/v1/parties', json=self.political_party)
    self.assertEqual(response.status_code, 201)
    response = self.app.get('/api/v1/parties')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample Ultiman', str(response.data))

  def test_get_specific_political_office(self):
    """
    Test Political Offices Get Specific
    """
    Political().create_political_party(
      "Sample 1", "Some Address", "example.com"
    )

    political_party = Political().create_political_party(
      "Sample 2", "Some Address", "example.com"
    )

    response = self.app.get('/api/v1/parties/' + str(political_party['party_id']))

    self.assertIn('Sample 2', str(response.data))
    self.assertNotIn('Sample 1', str(response.data))

  def test_edit_polotical_party(self):
    """
    Test Political Parties edit
    """
    political_party = Political().create_political_party(
      "Sample", "Some Address", "example.com")
    response = self.app.get('/api/v1/parties')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample', str(response.data))

    editted_party_data = { "name": "Sample Edit" }

    response = self.app.patch(
      '/api/v1/parties/' + str(political_party['party_id']), json=editted_party_data)
    self.assertEqual(response.status_code, 200)
    response = self.app.get('/api/v1/parties')
    self.assertNotIn('"Sample"', str(response.data))
    self.assertIn('"Sample Edit"', str(response.data))

  def test_delete_political_party(self):
    """
    Test Political Parties delete
    """
    party = Political().create_political_party(
      "Sample Delete", "Some Address", "example.com")
    response = self.app.get('/api/v1/parties')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample Delete', str(response.data))

    self.app.delete('/api/v1/parties/' + str(party['party_id']))
    self.assertEqual(response.status_code, 200)

    response = self.app.get('/api/v1/parties')
    self.assertEqual(response.status_code, 200)
    self.assertNotIn('Sample Delete', str(response.data))
