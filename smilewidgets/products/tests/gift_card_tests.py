from django.test import TestCase
import products.models
import products.serializers
from products import models, serializers
from products.models import GiftCard
from products.serializers import GiftCardSerializer


class GiftCardTest(TestCase):
    """Test cases for the GiftCard class"""

    def setUp(self):
        """Test case setup"""

        self.gift_card_attributes = {
            'code': '10OFF',
            'amount': 1000,
            'date_start': '2018-01-01',
            'date_end': '2019-01-01'
        }
        self.serializer_data = {
            'code': '30OFF',
            'amount': 3000,
            'date_start': '2018-01-01',
            'date_end': ''
        }

        self.gift_card = GiftCard.objects.create(**self.gift_card_attributes)
        self.serializer = GiftCardSerializer(instance=self.gift_card)

    def test_model_string_representation(self):
        """Verifies the output of the str method"""

        self.assertEqual(str(self.gift_card), '10OFF - $10.00')

    def test_serializer_contains_expected_fields(self):
        """Verifies that the serializer contains all of the fields it should and none of the fields it shouldn't"""

        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), ['code', 'amount', 'date_start', 'date_end'])

    def test_serializer_code_content(self):
        """Verifies the serializer contains the correct data in the 'code' field"""

        data = self.serializer.data

        self.assertEqual(data['code'], self.gift_card_attributes['code'])

    def test_serializer_amount_content(self):
        """Verifies the serializer contains the correct data in the 'amount' field"""

        data = self.serializer.data

        self.assertEqual(data['amount'], self.gift_card_attributes['amount'])

    def test_serializer_date_start_content(self):
        """Verifies the serializer contains the correct data in the 'date_start' field"""

        data = self.serializer.data

        self.assertEqual(data['date_start'],
                         self.gift_card_attributes['date_start'])

    def test_serializer_date_end_content(self):
        """Verifies the serializer contains the correct data in the 'date_end' field"""

        data = self.serializer.data

        self.assertEqual(data['date_end'],
                         self.gift_card_attributes['date_end'])
