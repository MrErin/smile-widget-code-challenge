from django.test import TestCase
import products.models
from products import models
from products.models import GiftCard


class GiftCardTest(TestCase):
    """Test cases for the GiftCard class"""

    def test_string_representation(self):
        """Verifies the output of the str method"""
        gift_card = GiftCard(code='10OFF', amount=1000,
                             date_start='2018-07-01')
        self.assertEqual(str(gift_card), '10OFF - $10.00')
