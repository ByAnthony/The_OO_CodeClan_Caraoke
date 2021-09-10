import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue = Venue("The Magestic", 20)

    def test_venue_has_name(self):
        self.assertEqual("The Magestic", self.venue.name)

    def test_venue_has_fee(self):
        self.assertEqual(20, self.venue.fee)