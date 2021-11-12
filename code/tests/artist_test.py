import unittest
from models.artist import Artist

class ArtistTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("David Bowie")

    def test_artist_has_name(self):
        self.assertEqual(self.artist_1.name, "David Bowie")