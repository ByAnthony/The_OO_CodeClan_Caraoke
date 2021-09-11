import unittest

from classes.guest import Guest
from classes.venue import Venue


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Tony", 150.00, "Toujours Plus Con")
        self.guest_2 = Guest("Will", 100.00, "Bohemian Rapsody")
        self.guest_3 = Guest("Calum", 150.00, "Could You Be Loved")
        self.guest_4 = Guest("Lewis", 200.00, "Flower Of Scotland")
        self.guest_5 = Guest("Jordan", 300.00, "I Was Made For Lovin You")

        self.venue = Venue("The Magestic")

    def test_guest_has_name(self):
        self.assertEqual("Lewis", self.guest_4.name)

    def test_guest_has_wallet(self):
        self.assertEqual(150.00, self.guest_1.wallet)