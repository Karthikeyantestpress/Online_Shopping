from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_templates_used_for_cart_detail_view(self):
        self.cart_detail_url = reverse("cart:cart_detail")

        response = self.client.get(self.cart_detail_url)
        self.assertTemplateUsed(response, "cart/detail.html")
