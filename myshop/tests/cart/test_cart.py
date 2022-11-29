from django.test import TestCase
from django.conf import settings
from tests.cart.test_model_mixin_testcase import ModelMixinTestcase


class Testurls(ModelMixinTestcase, TestCase):
    def test_initialize_cart_clean_session(self):

        self.assertEqual(self.cart.cart, {})

    def test_add_new_product_to_the_cart(self):
        self.cart.add_product(self.product, quantity=3)
        self.assertEqual(self.cart.cart["1"]["quantity"], 3)

    def test_increment_the_existing_product_in_cart(self):
        self.cart.add_product(self.product, quantity=5)
        self.cart.increment_product_quantity(self.product)
        self.assertEqual(self.cart.cart["1"]["quantity"], 6)

    def test_change_the_existing_product_quantity_in_cart(self):
        self.cart.add_product(self.product, quantity=5)
        self.cart.change_product_quantity(self.product, quantity=7)
        self.assertEqual(self.cart.cart["1"]["quantity"], 7)

    def test_remove_product_from_cart(self):
        self.cart.add_product(self.product, quantity=10)
        self.cart.remove_product(self.product)
        self.assertEqual(self.cart.cart, {})

    def test_total_price_Of_a_product_in_cart(self):
        self.cart.add_product(self.product, quantity=9)
        calculated_price = self.product.price * self.cart.cart["1"]["quantity"]

        self.assertEqual(self.cart.get_total_price(), calculated_price)
