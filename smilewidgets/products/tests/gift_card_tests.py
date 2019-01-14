from django.test import TestCase
from rest_framework.test import APIRequestFactory
from products.models import GiftCard
from products.serializers import GiftCardSerializer
from products.views import GiftCardViewSet


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

    def test_model_can_crete_gift_card(self):
        """Ensure the model will create a new entry in the table"""

        self.test_gift_card = GiftCard(
            code='500OFF-FAKE', amount=50000, date_start='2018-01-01', date_end='2018-12-31')

        old_count = GiftCard.objects.count()
        self.test_gift_card.save()
        new_count = GiftCard.objects.count()
        self.assertEqual(new_count, (old_count + 1))

    def test_gift_card_view_set(self):
        request = APIRequestFactory().get('')
        gift_card_detail = GiftCardViewSet.as_view({'get': 'retrieve'})
        gc = GiftCard.objects.create(
            code='500OFF-FAKE', amount=50000, date_start='2018-01-01', date_end='2018-12-31')
        response = gift_card_detail(request, pk=gc.pk)

        self.assertEqual(response.status_code, 200)
