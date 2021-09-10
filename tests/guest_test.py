import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Will", 200, "Bohemian Rapsodie")
        self.guest_2 = Guest("Callum", 100, "Could You Be Loved")
        self.guest_3 = Guest("Lewis", 300, "La Seine")
        self.guest_4 = Guest("Jordan", 500, "Born For One Thing")

        self.guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

        self.venue = Venue("The Magestic", 20)

    def test_guest_has_name(self):
        self.assertEqual("Will", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(300, self.guest_3.money)

    def test_sufficient_money__true_if_enough(self):
        self.assertEqual(True, self.guest_2.sufficient_money(self.venue))

    def test_sufficient_money__false_if_not_enough(self):
        poor_customer = Guest("Alex", 10, "Veiller Tard")
        self.assertEqual(False, poor_customer.sufficient_money(self.venue))

    def test_entry_fee(self):
        self.guest_1.entry_fee(self.venue)
        self.assertEqual(180, self.guest_1.money)