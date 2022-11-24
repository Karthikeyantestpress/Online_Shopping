from django.test import TestCase, Client
from shop.models import Product, Category
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
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
