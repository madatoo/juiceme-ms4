from django.test import TestCase
from .models import Product


class Test_product_name(TestCase):
    name = Product(name="New product")
    
    self.assertEqual(str(product_name), "New product")
