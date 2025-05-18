import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_valid(self):
        c = Customer("Eve")
        self.assertEqual(c.name, "Eve")

    def test_name_invalid_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_name_invalid_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("x" * 16)

    def test_create_order_and_coffees(self):
        from order import Order
        c = Customer("Zack")
        cf = Coffee("Espresso")
        c.create_order(cf, 4.0)
        self.assertEqual(len(c.orders()), 1)
        self.assertIn(cf, c.coffees())
