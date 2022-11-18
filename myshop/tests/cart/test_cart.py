from django.test import TestCase, RequestFactory
from cart.cart import Cart
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from shop.models import Product, Category


class Testurls(TestCase):
    def setUp(self):
        self.request = RequestFactory().get("/")

        # adding session
        middleware = SessionMiddleware(get_response=self.request)
        middleware.process_request(self.request)
        self.request.session.save()

        self.cart_obj = Cart(self.request)

        self.newcategory = Category.objects.create(
            name="Gaming",
            slug="gaming",
        )

        self.newproduct = Product.objects.create(
            category=self.newcategory,
            name="Play station 5",
            slug="play-station-5",
            description="A gaming console",
            price=50.000,
        )

    def test_add_product_returns_right(self):
        self.cart_obj.add_product(self.newproduct, quantity=3)
        cart_list = self.request.session.get(settings.CART_SESSION_ID)

        self.assertEqual(str(self.newproduct.price), cart_list["1"]["price"])

    def test_add_product_returns_(self):
        self.cart_obj.add_product(self.newproduct, quantity="21")
        cart_list = self.request.session.get(settings.CART_SESSION_ID)

        self.assertEqual(str(self.newproduct.price), cart_list["1"]["price"])

    def test_initialize_cart_clean_session(self):

        self.assertEqual(self.cart_obj.cart, {})
