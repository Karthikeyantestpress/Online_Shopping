from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import product_list, product_detail
from .test_model_mixin_testcase import ModelMixinTestCase


class Testurls(ModelMixinTestCase, SimpleTestCase):
    def test_product_list(self):
        self.product_list_url = reverse("shop:product_list")
        self.assertEqual((resolve(self.product_list_url).func), product_list)

    def test_product_list_by_category(self):
        self.product_list_category = reverse(
            "shop:product_list_by_category", args=[self.newcategory.slug]
        )
        self.assertEqual(
            (resolve(self.product_list_category).func), product_list
        )

    def test_product_detail(self):
        self.product_detail_url = reverse(
            "shop:product_detail",
            args=[self.newproduct.id, self.newproduct.slug],
        )
        self.assertEqual(
            (resolve(self.product_detail_url).func), product_detail
        )
