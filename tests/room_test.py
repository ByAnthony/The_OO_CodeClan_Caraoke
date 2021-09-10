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

        self.guest_1 = ["Will", 200, "Bohemian Rapsodie"]
        self.guest_2 = ["Callum", 100, "Could You Be Loved"]
        self.guest_3 = ["Lewis", 300, "La Seine"]
        self.guest_4 = ["Jordan", 500, "Born For One Thing"]
        self.guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

        self.song_1 = ["Vivants", "Noe Talbot"]
        self.song_2 = ["La Seine", "Vanessa Paradis"]
        self.song_3 = ["Rebecca", "Les Fatals Picards"]
        self.song_4 = ["Born For One Thing", "Gojira"]
        self.songs = [self.song_1, self.song_2, self.song_4]

        self.playlist = [self.song_1, self.song_2, self.song_3, self.song_4]

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