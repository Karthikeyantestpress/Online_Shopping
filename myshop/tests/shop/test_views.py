from django.test import TestCase
from django.urls import reverse
from .test_model_mixin_testcase import ModelMixinTestCase


class TestViews(ModelMixinTestCase, TestCase):
    def test_templates_used_for_product_list_view(self):
        self.product_list_url = reverse("shop:product_list")

        response = self.client.get(self.product_list_url)
        self.assertTemplateUsed(response, "shop/product/list.html")

    def test_templates_used_for_product_detail_view(self):
        self.product_detail_url = reverse(
            "shop:product_detail",
            args=[self.newproduct.id, self.newproduct.slug],
        )

        response = self.client.get(self.product_detail_url)
        self.assertTemplateUsed(response, "shop/product/detail.html")

    def test_return_404_for_invalid_slug(self):
        self.product_detail_url = reverse(
            "shop:product_detail",
            args=[self.newproduct.id, "invalid_slug"],
        )
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code, 404)
