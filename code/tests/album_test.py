import unittest

from models.artist import Artist
from models.album import Album

#  def __init__(self, artist, title, id = None):

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("David Bowie")
        self.album_1 = Album(self.artist_1, "Low")

    def test_album_has_artist(self):
        self.assertEqual(self.album_1.artist.name, "David Bowie")

    def test_album_has_title(self):
        self.assertEqual(self.album_1.suptitleport, "Low")
