"""
Tests for Political Party Model
"""
from unittest import TestCase
from app.api.v1.models.political_model import Political


class TestPoliticalPartyModel(TestCase):
  """
  TestPoliticalParty class
  """

  def test_political_party_create(self):
    """
    Test that PoliticalParty Model Creates Political Party
    """

    political_party = Political().create_political_party(
      "Some Party", "Adress", "example.com")

    political_parties = Political().get_political_parties()
    self.assertIn(political_party, political_parties)

  def test_get_specific_political_party(self):
    """
    Test that get_specific_political_party returns correct Party
    """
    political_party = Political().create_political_party(
      "Party A", "Address", "example.com")

    Political().create_political_party(
      "Party B", "Address", "example.com")

    returned_party = Political().get_specific_political_party(
      political_party["party_id"])
    self.assertEquals(political_party, returned_party)

  def test_delete_political_party(self):
    """
    Test that delete political party deletes party
    """

    political_party = Political().create_political_party(
      "Sample Party", "Adress", "example.com")

    political_parties = Political().get_political_parties()
    self.assertIn(political_party, political_parties)

    Political().delete_political_party(political_party["party_id"])
    political_parties = Political().get_political_parties()
    self.assertNotIn(political_party, political_parties)
