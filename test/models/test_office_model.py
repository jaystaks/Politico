"""
Tests for Office Model
"""
from unittest import TestCase
from app.api.v1.models.office import PoliticalOffice


class TestOfficeModel(TestCase):
  """
  TestOfficeModel class
  """

  def test_political_office_create(self):
    """
    Test that PoliticalOffice Model Creates Political Offices
    """

    political_office = PoliticalOffice().create_political_office(
      "Some Office", "Presidential")

    political_offices = PoliticalOffice().get_political_office()
    self.assertIn(political_office, political_offices)

  def test_get_specific_political_office(self):
    """
    Test that get_specific_political_office returns correct Office
    """
    political_office = PoliticalOffice().create_political_office(
      "Office B", "Presidential")

    PoliticalOffice().create_political_office(
      "Office A", "Presidential")

    returned_office = PoliticalOffice().get_specific_political_office(political_office["office_id"])
    self.assertEqual(political_office, returned_office)
