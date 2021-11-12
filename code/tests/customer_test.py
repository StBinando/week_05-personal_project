import unittest

from models.customer import Customer

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("John Smith", "+447857634091")

    def test_customer_has_name(self):
        self.assertEqual(self.customer_1.name, "John Smith")

    def test_customer_has_contact(self):
        self.assertEqual(self.customer_1.contact, "+447857634091")
