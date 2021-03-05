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

        self.song_list = [song1,song2,song3,song4,song5]

    # def test_get_song_list(self):

    #     self.assertEqual("Master Blaster,Under Pressure,One,Sweet Child Of Mine,Help,Beat It",)