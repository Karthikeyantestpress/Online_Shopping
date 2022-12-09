from django.test import SimpleTestCase
from django.urls import reverse, resolve
from coupons.views import coupon_apply



class Testurls(SimpleTestCase):
    def test_coupon_apply(self):
        product_list_url = reverse("coupons:apply")
        self.assertEqual((resolve(product_list_url).func), coupon_apply)