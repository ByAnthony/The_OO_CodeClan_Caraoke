import unittest

from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Vivants", "Noe Talbot")
        self.song_2 = Song("Rebecca", "Les Fatals Picards")
        self.song_3 = Song("Tournent Les Violons", "Jean-Jacques Goldman")

    def test_song_has_title(self):
        self.assertEqual("Tournent Les Violons", self.song_3.title)

    def test_song_has_artist(self):
        self.assertEqual("Les Fatals Picards", self.song_2.artist)