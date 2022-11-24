from django.test import TestCase
from .test_modelmixintestcase import ModelMixinTestCase
from django.urls import reverse


class TestModelMethod(ModelMixinTestCase, TestCase):
    def test_absolute_url_in_category_model(self):
        self.product_list_category = reverse(
            "shop:product_list_by_category", args=[self.newcategory.slug]
        )
        self.assertEqual(
            self.product_list_category, self.newcategory.get_absolute_url()
        )

    def test_absolute_url_in_product_model(self):
        self.product_detail_view = reverse(
            "shop:product_detail",
            args=[self.newproduct.id, self.newproduct.slug],
        )
        self.assertEqual(
            self.product_detail_view, self.newproduct.get_absolute_url()
        )
