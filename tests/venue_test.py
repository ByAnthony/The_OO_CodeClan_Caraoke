import unittest

from classes.venue import Venue

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue = Venue("The Magestic")

    def test_venue_has_name(self):
        self.assertEqual("The Magestic", self.venue.name)