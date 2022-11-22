from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from cart.cart import Cart
from shop.models import Product, Category
from coupons.models import Coupon
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal


class ModelMixinTestcase(TestCase):
    def setUp(self):
        self.request = RequestFactory().get("/")
        middleware = SessionMiddleware(get_response=self.request)
        middleware.process_request(self.request)

        self.request.session.save()

        self.cart = Cart(self.request)

        self.category = Category.objects.create(
            name="Gaming",
            slug="gaming",
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Play station 5",
            slug="play-station-5",
            description="A gaming console",
            price=50.000,
        )

        self.coupon = Coupon.objects.create(
            code="firsttime",
            valid_from=timezone.now() - timedelta(30),
            valid_to=timezone.now() + timedelta(30),
            discount=50,
            active=True,
        )
        self.discount_percent = self.coupon.discount / Decimal(100)
