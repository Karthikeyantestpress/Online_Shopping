from django.test import TestCase, RequestFactory
from shop.models import Product, Category
from django.contrib.sessions.middleware import SessionMiddleware
from cart.cart import Cart
from myshop.settings import CART_SESSION_ID


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.newcategory = Category.objects.create(
            name="Gaming",
            slug="gaming",
        )
        self.newcategory2 = Category.objects.create(
            name="Books",
            slug="books",
        )

        self.newproduct = Product.objects.create(
            category=self.newcategory,
            name="Play station 5",
            slug="play-station-5",
            description="A gaming console",
            price=50.000,
        )
        self.newproduct_2 = Product.objects.create(
            category=self.newcategory2,
            name="Clean Code",
            slug="clean-code",
            description="A book about how to write a clean code",
            price=25,
        )

