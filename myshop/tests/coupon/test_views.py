from django.test import TestCase, RequestFactory
from django.urls import reverse
from cart.cart import Cart
from coupons.views import coupon_apply
from orders.views import order_create
from orders.models import Order
from django.contrib.sessions.middleware import SessionMiddleware
from tests.cart.test_model_mixin_testcase import ModelMixinTestcase


class TestViews(ModelMixinTestcase, TestCase):
    def get_request(self, method, data):
        request = RequestFactory().get("/")
        middleware = SessionMiddleware(get_response=request)
        middleware.process_request(request)
        request.session.save()
        request.method = method
        request.POST = data
        return request

    def create_cart(self, request, product, quantity):
        cart = Cart(request)
        cart.add_product(product, quantity)
        cart.coupon_id = self.coupon.code
        return cart

    def test_templates_for_coupon_apply_redirects_to_cart_detail(self):

        response = self.client.post(reverse("coupons:apply"))
        self.assertEqual(response.url, reverse("cart:cart_detail"))

    def test_applying_a_valid_coupon_succeeds_order_with_discount_price(self):

        request = self.get_request(
            method="POST",
            data={
                "code": self.coupon.code,
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@example.ocm",
                "address": "132, Main street, New town",
                "postal_code": "782032",
                "city": "Gowtham city",
            },
        )
        coupon_apply(request)
        self.create_cart(request, product=self.product, quantity=2)
        order_create(request)
        order = Order.objects.filter(id=1)[0]
        total_cost = self.product.price * 1
        discount_price = total_cost * (order.discount / 100)
        excepted_total_cost = total_cost - discount_price

        self.assertEqual(excepted_total_cost, order.get_total_cost())
