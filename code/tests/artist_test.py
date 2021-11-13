import unittest
from models.artist import Artist

class ArtistTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("Bowie", "David")
        self.artist_2 = Artist("Madonna")

    def test_artist_has_full_name(self):
        first_name = self.artist_1.first_name
        full_name = ("" if first_name == None else first_name+" ")+self.artist_1.last_name
        self.assertEqual(full_name, "David Bowie")

    def test_artist_has_full_name(self):
        first_name = self.artist_2.first_name
        full_name = ("" if first_name == None else first_name+" ")+self.artist_2.last_name
        self.assertEqual(full_name, "Madonna")
