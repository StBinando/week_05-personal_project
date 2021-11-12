import unittest

from models.artist import Artist
from models.album import Album
from models.item import Item

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("David Bowie")
        self.album_1 = Album(self.artist_1, "Low")
        self.item_1 = Item(self.album_1, "CD", 6.50, 9.99, 7, 2)

    def test_item_has_album(self):
        self.assertEqual(self.item_1.album.artist.name, "David Bowie")

    def test_item_has_support(self):
        self.assertEqual(self.item_1.support, "CD")

    def test_item_has_cost(self):
        self.assertEqual(self.item_1.cost, 6.50)

    def test_item_has_selling_price(self):
        self.assertEqual(self.item_1.selling_price, 9.99)

    def test_item_has_in_stock_value(self):
        self.assertEqual(self.item_1.in_stock, 7)

    def test_item_has_ordered_value(self):
        self.assertEqual(self.item_1.ordered, 2)


