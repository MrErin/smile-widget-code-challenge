from django.test import TestCase
import products.models
from products import models
from products.models import ProductPrice


class ProductPriceTest(TestCase):
    """Tests cases for the ProductPrice class"""

    def test_string_representation(self):
        """Verifies the output of the str method"""
        product_price = ProductPrice(
            code='big_widget', price=80000, price_start_date='2018-11-23', price_end_date='2018-11-25')
        self.assertEqual(str(
            product_price), 'Code: big_widget; Price: $800.00; Price start date: 2018-11-23; Price end date: 2018-11-25')
