from django.test import TestCase, RequestFactory
from cart.cart import Cart
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from shop.models import Product, Category


class Testurls(TestCase):
    def setUp(self):
        self.request = RequestFactory().get("/")
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

    def test_initialize_cart_clean_session(self):
       

        self.assertEqual(self.cart_obj.cart, {})

    def test_add_new_product_to_the_cart(self):
        self.cart_obj.add_product(self.newproduct, quantity=3)
        cart_list = self.request.session.get(settings.CART_SESSION_ID)
        
        self.assertEqual(cart_list["1"]["quantity"],3)

    def test_increment_the_existing_product_in_cart(self):
        self.cart_obj.add_product(self.newproduct, quantity=5)
        self.cart_obj.increment_product_quantity(self.newproduct)
        cart_list = self.request.session.get(settings.CART_SESSION_ID)
        self.assertEqual(cart_list["1"]["quantity"],6)

    def test_change_the_existing_product_quantity_in_cart(self):
        self.cart_obj.add_product(self.newproduct, quantity=5)
        self.cart_obj.change_product_quantity(self.newproduct,quantity=7)
        cart_list = self.request.session.get(settings.CART_SESSION_ID)
        self.assertEqual(cart_list["1"]["quantity"],7)
    
    def test_remove_product_from_cart(self):
        self.cart_obj.add_product(self.newproduct, quantity=10)
        self.cart_obj.remove_product(self.newproduct)
        cart_list = self.request.session.get(settings.CART_SESSION_ID)
        self.assertEqual(cart_list,{})

    def test_total_price_Of_a_product_in_cart(self):
        self.cart_obj.add_product(self.newproduct, quantity=9)
        Total_price=self.cart_obj.get_total_price()
        cart_list = self.request.session.get(settings.CART_SESSION_ID)
        self.assertEqual(Total_price,self.newproduct.price*cart_list["1"]["quantity"])
        
    
 


