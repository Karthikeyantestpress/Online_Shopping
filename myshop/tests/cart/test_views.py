from django.test import TestCase
from django.urls import reverse
from tests.cart.test_model_mixin_testcase import ModelMixinTestcase


class TestViews(ModelMixinTestcase, TestCase):
    def test_templates_used_for_cart_detail_view(self):
        cart_detail_url = reverse("cart:cart_detail")

        response = self.client.get(cart_detail_url)
        self.assertTemplateUsed(response, "cart/detail.html")

    def test_cart_add_returns_302_for_valid_product(self):
        reponse = self.client.post(reverse("cart:cart_add", args=[1]))
        self.assertEqual(reponse.status_code, 302)

    def test_cart_add_returns_404_for_invalid_product(self):
        reponse = self.client.post(reverse("cart:cart_add", args=[10]))
        self.assertEqual(reponse.status_code, 404)

    def test_cart_add_returns_redirect_to_cart_detail_for_valid_product(self):
        response = self.client.post(reverse("cart:cart_add", args=[1]))
        self.assertEqual(response.url, reverse("cart:cart_detail"))

    def test_cart_remove_returns_redirect_to_cart_detail_for_valid_product(
        self,
    ):
        response = self.client.post(reverse("cart:cart_remove", args=[1]))
        self.assertEqual(response.url, reverse("cart:cart_detail"))

    def test_cart_remove_returns_404_for_invalid_product(self):
        response = self.client.post(reverse("cart:cart_remove", args=[10]))
        self.assertEqual(response.status_code, 404)
