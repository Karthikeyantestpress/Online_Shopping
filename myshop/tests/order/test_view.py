from django.test import TestCase
from tests.shop.test_modelmixintestcase import ModelMixinTestCase
from django.urls import reverse


class Testcreateview(ModelMixinTestCase, TestCase):
    def test_order_create_template_when_http_method_is_post(self):
        self.Order_Create_url = reverse("orders:order_create")

        response = self.client.get(self.Order_Create_url)
        self.assertTemplateUsed(response, "orders/order/create.html")

    def test_order_create_template_when_http_method_is_get(self):
        self.Order_Create_url = reverse("orders:order_create")

        responsey = self.client.post(
            self.Order_Create_url,
            {
                "first_name": "john",
                "last_name": "smith",
                "email": "deepak@gmail.com",
                "address": "122,anhd, asjs,ask",
                "postal_code": "605 110",
                "city": "chennai",
            },
        )

        self.assertTemplateUsed(responsey, "orders/order/created.html")
