import unittest

from models.artist import Artist
from models.album import Album

class AlbumTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("Bowie", "David")
        self.album_1 = Album(self.artist_1, "Low")

    def test_album_has_artist(self):
        self.assertEqual(self.album_1.artist.last_name, "Bowie")

    def test_album_has_title(self):
        self.assertEqual(self.album_1.title, "Low")
