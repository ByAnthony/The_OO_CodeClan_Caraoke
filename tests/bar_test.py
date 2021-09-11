import unittest

from classes.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Bar("Irn Bru", 2.00)
        self.drink_2 = Bar("Rince Cochon", 5.00)
        self.drink_3 = Bar("Chablis", 10.00)

    def test_bar_has_drink(self):
        self.assertEqual("Irn Bru", self.drink_1.drink)

    def test_bar_has_price(self):
        self.assertEqual(10.00, self.drink_3.price)