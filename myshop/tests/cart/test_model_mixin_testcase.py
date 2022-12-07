from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from cart.cart import Cart
from shop.models import Product, Category


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
