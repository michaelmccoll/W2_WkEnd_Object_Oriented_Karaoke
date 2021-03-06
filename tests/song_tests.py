import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Master Blaster","Stevie Wonder")
        self.song2 = Song("Under Pressure","Queen")
        self.song3 = Song("One","U2")
        self.song4 = Song("Sweet Child Of Mine","Guns N Roses")
        self.song5 = Song("Help","The Beatles")
        self.song6 = Song("Beat It","Michael Jackson")

    # Tests it can get songs name
    def test_song_name(self):                                   
        self.assertEqual("Help", self.song5.song_name)

    # Tests it can get song artist
    def test_artist(self):                                      
        self.assertEqual("U2", self.song3.artist)