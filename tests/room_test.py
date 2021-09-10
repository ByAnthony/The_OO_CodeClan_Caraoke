import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Toolbooth", 3)
        self.room_2 = Room("Barra", 10)
        self.room_3 = Room("Green", 15)

        self.guest_1 = Guest("Will", 200, "Bohemian Rapsodie")
        self.guest_2 = Guest("Callum", 100, "Could You Be Loved")
        self.guest_3 = Guest("Lewis", 300, "La Seine")
        self.guest_4 = Guest("Jordan", 500, "Born For One Thing")
        self.guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

        self.song_1 = Song("Vivants")
        self.song_2 = Song("La Seine")
        self.song_3 = Song("Rebecca")
        self.song_4 = Song("Born For One Thing")
        self.songs = [self.song_1, self.song_2, self.song_4]

        self.room_playlist = [self.song_1, self.song_2, self.song_3, self.song_4]

    def test_room_has_name(self):
        self.assertEqual("Green", self.room_3.name)

    def test_room_has_guest_number(self):
        self.assertEqual(10, self.room_2.guest_number)

    def test_room_has_no_guests(self):
        self.assertEqual(None, self.room_1.guest_count())

    def test_room_check_in(self):
        self.room_2.check_in(self.guests)
        self.assertEqual(4, self.room_2.guest_count())

    def test_room_check_in__room_capacity_exceeded(self):
        self.room_1.check_in(self.guests)
        self.assertEqual("This room is too small for your group. Please book a room with a greater capacity", self.room_1.check_in(self.guests))

    def test_room_check_out(self):
        self.room_3.check_in(self.guests)
        self.room_3.check_out(self.guests)
        self.assertEqual(None, self.room_3.guest_count())

    def test_add_songs(self):
        self.room_2.add_songs(self.songs)
        self.assertEqual(3, self.room_2.song_count())

    def test_guest_has_favorite_song(self):
        self.assertEqual("Born For One Thing", self.guest_4.favorite_song)

    def test_find_favorite_song(self):
        self.assertEqual("Whoo!", self.room_3.find_favorite_song(self.songs, self.guest_3.favorite_song))