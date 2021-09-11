import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.venue = Venue("The Magestic")

        self.room_1 = Room("Toolboth", ["Toujours Plus Con", "La Seine", "Capitaine Abandonne"], 3, 5.00)
        self.room_2 = Room("Barra", ["One More Time", "Oxygene", "Un Autre Monde"], 8, 9.00)
        self.room_3 = Room("Green", ["Quand La Ville Dort", "Dans Mon Verre", "Je Marche Seul"], 15, 13.00)

        self.song_1 = Song("Les Lacs du Connemara", "Michel Sardou")
        self.song_2 = Song("Le Jour S'Est Leve", "Telephone")

        self.guest_1 = Guest("Tony", 150.00, "Toujours Plus Con")
        self.guest_2 = Guest("Will", 100.00, "Bohemian Rapsody")
        self.guest_3 = Guest("Calum", 150.00, "Could You Be Loved")
        self.guest_4 = Guest("Lewis", 200.00, "Flower Of Scotland")
        self.guest_5 = Guest("Jordan", 300.00, "I Was Made For Lovin You")

    def test_room_has_number(self):
        self.assertEqual("Barra", self.room_2.name)   

    def test_room_has_song_list(self):
        self.assertEqual(["Toujours Plus Con", "La Seine", "Capitaine Abandonne"], self.room_1.playlist)

    def test_check_in_guest(self):
        self.room_1.check_in_guests(self.guest_1)
        self.room_1.check_in_guests(self.guest_2)
        self.room_1.check_in_guests(self.guest_3)
        self.assertEqual(3, self.room_1.guest_count())

    def test_check_out_guest(self):
        self.room_2.check_in_guests(self.guest_3)
        self.room_2.check_in_guests(self.guest_4)
        self.room_2.check_out_guests(self.guest_3)
        self.room_2.check_out_guests(self.guest_4)
        self.assertEqual(0, self.room_2.guest_count())

    def test_add_song(self):
        self.assertEqual(["Quand La Ville Dort", "Dans Mon Verre", "Je Marche Seul", "Les Lacs du Connemara"], self.room_3.add_song(self.song_1.title))

    def test_check_in_guest__capacity_not_reached(self):
        self.room_1.check_in_guests(self.guest_1)
        self.room_1.check_in_guests(self.guest_2)
        self.assertEqual(2, self.room_1.guest_count())

    def test_check_in_guest__capacity_exceeded(self):
        self.room_1.check_in_guests(self.guest_3)
        self.room_1.check_in_guests(self.guest_4)
        self.room_1.check_in_guests(self.guest_5)
        self.room_1.check_in_guests(self.guest_2)
        self.assertEqual(4, self.room_1.guest_count())

    def test_guest_has_favorite_song(self):
        self.assertEqual("Flower Of Scotland", self.guest_4.favorite_song)

    def test_find_favorite_song(self):
        self.assertEqual("Whoo!", self.room_1.find_favorite_song(self.guest_1.favorite_song))

    def test_guest_entry_fee(self):
        self.room_2.check_in_guests(self.guest_1)
        self.assertEqual(9, self.room_2.till)
        self.assertEqual(141.00, self.guest_1.wallet)