from django.test import TestCase
import products.models
from products import models
from products.models import Product


class ProductTest(TestCase):
    """Test cases for the Product class"""

    def test_string_representation(self):
        """Verifies the output of the str method"""
        product = Product(name='Big Widget', code='big_widget')
        self.assertEqual(str(product), 'Big Widget - big_widget')
