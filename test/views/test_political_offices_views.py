"""
Tests for Political Offices Views
"""
from instance.config import appConfig
from app import politico
from unittest import TestCase
from app.api.v1.models.office import PoliticalOffice


class TestPoliticalOfficesViews(TestCase):
  """
  Test Political Offices Views Class
  """
  def setUp(self):
      self.app = politico('testing').test_client()
      self.political_office = {"name": "Sample", "office_type": "Presidential"}

  def test_get_polotical_office(self):
    """
    Test Political Offices GET
    """
    PoliticalOffice().create_political_office(
      "Sample Get", "Presidential")
    response = self.app.get('/api/v1/office')
    retrieved_political_offices = response.data
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample Get', str(response.data))

  def test_create_political_office(self):
    """
    Test Political Offices Create
    """
    PoliticalOffice().create_political_office(
      "Sample", "office_type")
    response = self.app.post(
      '/api/v1/office', json=self.political_office)
    #self.assertEqual(response.status_code, 200)
    response = self.app.get('/api/v1/office')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample', str(response.data))

  def test_get_specific_political_office(self):
    """
    Test Political Offices Get Specific
    """
    PoliticalOffice().create_political_office(
      "Sample 1", "Presidential"
    )

    political_office= PoliticalOffice().create_political_office(
      "Sample 2", "Presidential"
    )

    response = self.app.get('/api/v1/office/' + str(political_office['office_id']))

    self.assertIn('Sample 2', str(response.data))
    self.assertNotIn('Sample 1', str(response.data))
