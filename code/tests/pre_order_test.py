import unittest

from models.artist import Artist
from models.album import Album
from models.item import Item
from models.customer import Customer
from models.pre_order import PreOrder

class PreOrderTest(unittest.TestCase):
    def setUp(self):
        self.artist_1 = Artist("David Bowie")
        self.album_1 = Album(self.artist_1, "Low")
        self.item_1 = Item(self.album_1, "CD", 6.50, 9.99, 7, 2, 1)
        self.customer_1 = Customer("John Smith", "+447857634091")
        self.pre_order_1 = PreOrder(self.customer_1, self.item_1)

    def test_pre_order_has_item(self):
        self.assertEqual(self.pre_order_1.customer.name, "John Smith") 
    
    def test_pre_order_has_album(self):
        self.assertEqual(self.pre_order_1.item.album.artist.name, "David Bowie") 