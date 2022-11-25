from django.test import TestCase
from django.urls import reverse
from .test_model_mixin_testcase import ModelMixinTestCase
from shop.models import Product


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
            args=[self.newproduct.id, "invalid_product_slug"],
        )
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code, 404)

    def test_post_list_shows_all_product_when_category_not_selected(self):
        self.all_products = Product.objects.all()
        request = self.client.get(reverse("shop:product_list"))
        response = request.context.get("products")
        self.assertQuerysetEqual(self.all_products, response)

    def test_post_list_shows_category_based_products_when_category_is_selected(
        self,
    ):
        self.category_book = Product.objects.filter(category=self.newcategory2)
        request = self.client.get(
            reverse("shop:product_list_by_category", args=["books"])
        )
        response = request.context.get("products")
        self.assertQuerysetEqual(self.category_book, response)

    def test_post_list_shows_404_when_category_does_not_exists(self):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category", args=["invalid_category_slug"]
            )
        )
        self.assertEquals(response.status_code, 404)
