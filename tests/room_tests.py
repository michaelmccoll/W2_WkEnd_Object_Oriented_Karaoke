import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Nighties Room")      # may need 2 other variables 'guest_list' and 'song_list'
        self.room2 = Room("Eighties Room")
        self.room3 = Room("Seventies Room")

    def test_room_name(self):
        self.assertEqual("Eighties Room", self.room2.room_name)

    def test_check_in(self):                    # Tests that guest4 has been added to room3 guest_list
        guest4 = Guest("Max Power","Master Blaster")
        self.room3.check_in(guest4.guest_name)
        self.assertEqual(["Max Power"],self.room3.guest_list)

    def test_check_out(self):
        guest4 = Guest("Max Power","Master Blaster")
        self.room3.check_in(guest4.guest_name)
        self.room3.check_out(guest4.guest_name)
        self.assertEqual(0, self.room3.count_guests_in_room())



    # def test_count_guests_in_room(self):
    #     guest_list_total = self.room3.count_guests_in_room(self.room3)
    #     self.assertEqual(1,guest_list_total)

    
    # def tes_check_out(self):
    # remove guest from guest_list[]

    # def test_add_songs_to_rooms(self):
    # add songs to song_list[]