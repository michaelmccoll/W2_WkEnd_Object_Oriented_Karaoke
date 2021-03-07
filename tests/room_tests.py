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
        self.guest4 = Guest("Emma Wright","Dancing Queen",3)

    # Tests it can get room name
    def test_room_name(self):
        self.assertEqual("Eighties Room", self.room2.room_name)

    # Tests that guest4 has been added to room3 guest_list
    def test_check_in(self):                    
        guest4 = Guest("Max Power","Master Blaster",55)
        self.room3.check_in(guest4.guest_name)
        self.assertEqual(["Max Power"],self.room3.guest_list)

    # Tests that guest4 is checked in (added to room3 guest_list) and checked out (removed from room3 guest_list)
    def test_check_out(self):
        guest4 = Guest("Max Power","Master Blaster",55)
        self.room3.check_in(guest4.guest_name)
        self.room3.check_out(guest4.guest_name)
        self.assertEqual(0, self.room3.count_guests_in_room())

    # Tests that song7 is added to room1
    def test_add_songs_to_rooms(self):
        song7 = Song("Whatever","Oasis")
        self.room1.add_song_to_room(song7.song_name)
        self.assertEqual(["Whatever"],self.room1.song_list)

    def test_fee_transaction(self):
        self.room3.fee_transaction(self.room3.fee)
        self.assertEqual(5, self.room3.till)

    # Tests the advanced check in function, checks the guest_list if correct
    def test_check_in_advanced_enough_capacity(self):
        self.room3.check_in_advanced(self.guest1)
        self.room3.check_in_advanced(self.guest2)
        self.assertEqual(["Michael McColl","John Smith"],self.room3.guest_list)

    # Tests that it checks guests in, until capcacity full & returns full message, guest3 does not get checked in, wallets are reduced if guest checked-in
    def test_check_in_advanced_capacity_full(self):
        self.room3.check_in_advanced(self.guest1)
        self.room3.check_in_advanced(self.guest2)
        self.room3.check_in_advanced(self.guest3)
        self.assertEqual(["Michael McColl","John Smith"],self.room3.guest_list)
        self.assertEqual(95,self.guest1.wallet)
        self.assertEqual(70,self.guest2.wallet)
        self.assertEqual(50,self.guest3.wallet)

    # Tests that guest4 doesn't get checked in (as wallet doesn't have enough to pay fee) and guest2 doesn't get checked in (as room3 capacity full)
    def test_check_in_advanced_guest_cant_pay_and_capacity_full(self):
        self.room3.check_in_advanced(self.guest1)
        self.room3.check_in_advanced(self.guest4)
        self.room3.check_in_advanced(self.guest3)
        self.room3.check_in_advanced(self.guest2)
        self.assertEqual(["Michael McColl","Lisa Jones"],self.room3.guest_list)
        self.assertEqual(95,self.guest1.wallet)
        self.assertEqual(3,self.guest4.wallet)
        self.assertEqual(45,self.guest3.wallet)
        self.assertEqual(75,self.guest2.wallet)
        self.assertEqual(10,self.room3.till)