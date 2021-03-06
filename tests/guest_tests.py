import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Michael McColl","Help",100)
        self.guest2 = Guest("John Smith","Beat It",75)
        self.guest3 = Guest("Lisa Jones","Under Pressure",50)

    def test_guest_name(self):                                          # Tests it can get guests name
        self.assertEqual("Michael McColl", self.guest1.guest_name)

    def test_guest_fav_song(self):                                      # Tests it can get guest fav song
        self.assertEqual("Under Pressure", self.guest3.fav_song)

    def test_guest_list(self):                                          # Tests it can create a guest list and get guests names
        guest_list = [self.guest1.guest_name,self.guest2.guest_name,self.guest3.guest_name]
        self.assertEqual(["Michael McColl","John Smith","Lisa Jones"],guest_list)
    
    def test_reduce_wallet(self):
        self.guest3.reduce_wallet(10)
        self.assertEqual(40, self.guest3.wallet)