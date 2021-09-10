import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.venue import Venue 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Vivants", "Noe Talbot")
        self.song_2 = Song("La Seine", "Vanessa Paradis")
        self.song_3 = Song("Rebecca", "Les Fatals Picards")
        self.song_4 = Song("Born For One Thing", "Gojira")

    def test_song_has_title(self):
        self.assertEqual("Rebecca", self.song_3.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Vanessa Paradis", self.song_2.artist)

    