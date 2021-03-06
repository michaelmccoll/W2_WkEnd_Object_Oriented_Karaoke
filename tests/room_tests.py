import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Nighties Room",6,10)
        self.room2 = Room("Eighties Room",4,10)
        self.room3 = Room("Seventies Room",2,5)

        self.guest1 = Guest("Michael McColl","Help",100)
        self.guest2 = Guest("John Smith","Beat It",75)
        self.guest3 = Guest("Lisa Jones","Under Pressure",50)

    def test_room_name(self):
        self.assertEqual("Eighties Room", self.room2.room_name)

    def test_check_in(self):                    # Tests that guest4 has been added to room3 guest_list
        guest4 = Guest("Max Power","Master Blaster",55)
        self.room3.check_in(guest4.guest_name)
        self.assertEqual(["Max Power"],self.room3.guest_list)

    def test_check_out(self):                   # Tests that guest4 is checked in (added to room3 guest_list) and checked out (removed from room3 guest_list)
        guest4 = Guest("Max Power","Master Blaster",55)
        self.room3.check_in(guest4.guest_name)
        self.room3.check_out(guest4.guest_name)
        self.assertEqual(0, self.room3.count_guests_in_room())

    def test_add_songs_to_rooms(self):          # Tests that song7 is added to room1
        song7 = Song("Whatever","Oasis")
        self.room1.add_song_to_room(song7.song_name)
        self.assertEqual(["Whatever"],self.room1.song_list)

    def test_check_in_advanced(self):                    # Tests the advanced check in function
        # guest5 = Guest("Robert Smith","Master Blaster",55)
        self.room3.check_in_advanced(self.guest1.guest_name)
        self.room3.check_in_advanced(self.guest2.guest_name)
        self.room3.check_in_advanced(self.guest3.guest_name)
        print(self.room3.guest_list)
        self.assertEqual(["Michael McColl","John Smith"],self.room3.guest_list)
        # This is almost working, room3 guest list seems empty and it should have 2 guests

        # could maybe re-write function to take in room_name and guest_name
        # check_in_advanced(room_name,guest_name)