import unittest

from classes.guest import Guest
from classes.venue import Venue
from classes.bar import Bar


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Tony", 150.00, "Toujours Plus Con")
        self.guest_2 = Guest("Will", 100.00, "Bohemian Rapsody")
        self.guest_3 = Guest("Calum", 150.00, "Could You Be Loved")
        self.guest_4 = Guest("Lewis", 200.00, "Flower Of Scotland")
        self.guest_5 = Guest("Jordan", 300.00, "I Was Made For Lovin You")

        self.drink_1 = Bar("Irn Bru", 2.00)
        self.drink_2 = Bar("Rince Cochon", 5.00)
        self.drink_3 = Bar("Chablis", 10.00)

    def test_guest_has_name(self):
        self.assertEqual("Lewis", self.guest_4.name)

    def test_guest_has_wallet(self):
        self.assertEqual(150.00, self.guest_1.wallet)

    def test_guest_can_buy_drink__decreases_money(self): 
        self.guest_5.buy_drink(self.drink_2)
        self.assertEqual(295.00, self.guest_5.wallet)

    def test_guest_cannot_buy_if_insufficient_money(self):
        poor_guest = Guest("Alex", 1.00, "Voulez-Vous")
        poor_guest.buy_drink(self.drink_3)
        self.assertEqual(1.00, poor_guest.wallet)