from django.test import TestCase
from django.urls import reverse
from tests.cart.test_model_mixin_testcase import ModelMixinTestcase




class TestViews(ModelMixinTestcase,TestCase):
    def test_templates_for_coupon_apply_redirects_to_cart_detail(self):

        response = self.client.post(reverse("coupons:apply"))
        self.assertEqual(response.url, reverse("cart:cart_detail"))

    def test_total_price_of_the_product_after_using_discount_coupon(self):

        self.cart.add_product(self.product, quantity=9)
        calculated_total_price_with_discount =self.product.price * self.cart.cart["1"]["quantity"] *self.discount_percent
        self.assertEqual(self.cart.get_total_price_after_discount()/2, calculated_total_price_with_discount)

   

