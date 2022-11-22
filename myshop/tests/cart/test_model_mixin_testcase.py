from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from cart.cart import Cart
from shop.models import Product, Category
from coupons.models import Coupon



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

        self.coupon=Coupon.objects.create(code ="firsttime",
        valid_from="2022-12-09 03:35",
        valid_to="2023-10-10 07:35",
        discount=50, 
        active=True,
        )
        self.discount_percent = self.coupon.discount/100

