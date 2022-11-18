from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import cart_add, cart_detail


class Testurls(SimpleTestCase):
    def test_cart_add(self):
        self.cart_add_url = reverse("cart:cart_add", args=[1])
        self.assertEqual((resolve(self.cart_add_url).func), cart_add)

    def test_cart_detail(self):
        self.cart_detail_url = reverse("cart:cart_detail")
        self.assertEqual((resolve(self.cart_detail_url).func), cart_detail)
