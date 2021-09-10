import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Vivants")
        self.song_2 = Song("La Seine")
        self.song_3 = Song("Rebecca")
        self.song_4 = Song("Born For One Thing")

    def test_song_has_title(self):
        self.assertEqual("Rebecca", self.song_3.title)