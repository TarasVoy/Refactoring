import unittest
from user import User
from product import Product
from order import Order

class TestOnlineStore(unittest.TestCase):

    def test_user_register(self):
        user = User("john", "john@example.com")
        self.assertEqual(user.register(), "User john registered.")

    def test_user_login(self):
        user = User("jane", "jane@example.com")
        self.assertEqual(user.login(), "User jane logged in.")

    def test_add_order_to_user(self):
        user = User("kate", "kate@example.com")
        order = Order()
        user.add_order(order)
        self.assertEqual(len(user.view_orders()), 1)

    def test_add_product_to_order(self):
        product = Product("Laptop", 1200)
        order = Order()
        order.add_product(product)
        self.assertIn(product, order.products)

    def test_remove_product_from_order(self):
        product = Product("Phone", 800)
        order = Order()
        order.add_product(product)
        order.remove_product(product)
        self.assertNotIn(product, order.products)

    def test_calculate_total_single_product(self):
        product = Product("Monitor", 300)
        order = Order()
        order.add_product(product)
        self.assertEqual(order.calculate_total(), 300)

    def test_calculate_total_multiple_products(self):
        order = Order()
        order.add_product(Product("Keyboard", 100))
        order.add_product(Product("Mouse", 50))
        self.assertEqual(order.calculate_total(), 150)

    def test_order_linked_to_user(self):
        user = User("max", "max@example.com")
        order = Order()
        user.add_order(order)
        self.assertIn(order, user.orders)

    def test_view_empty_orders(self):
        user = User("sara", "sara@example.com")
        self.assertEqual(user.view_orders(), [])

    def test_order_total_empty(self):
        order = Order()
        self.assertEqual(order.calculate_total(), 0)
        
if __name__ == "__main__":
    unittest.main()