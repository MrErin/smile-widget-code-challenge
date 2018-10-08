from django.test import TestCase
from products.models import ProductPrice
from products.serializers import ProductPriceSerializer


class ProductPriceTest(TestCase):
    """Tests cases for the ProductPrice class"""

    def setUp(self):
        """Test case setup"""

        self.product_price_attributes = {
            'code': 'sm_widget',
            'price': 9900,
            'price_start_date': '2018-01-01',
            'price_end_date': '2018-12-31'
        }

        self.product_price = ProductPrice.objects.create(
            **self.product_price_attributes)
        self.serializer = ProductPriceSerializer(instance=self.product_price)

    def test_model_string_representation(self):
        """Verifies the output of the str method"""

        self.assertEqual(str(
            self.product_price), 'Code: sm_widget; Price: $99.00; Price start date: 2018-01-01; Price end date: 2018-12-31')

    def test_serializer_contains_expected_fields(self):
        """Verifies that the serializer contains all of the fields it should and none of the fields it shouldn't"""

        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), ['code', 'price', 'price_start_date', 'price_end_date'])

    def test_serializer_code_content(self):
        """Verifies the serializer contains the correct data in the 'code' field"""

        data = self.serializer.data

        self.assertEqual(data['code'], self.product_price_attributes['code'])

    def test_serializer_price_content(self):
        """Verifies the serializer contains the correct data in the 'price' field"""

        data = self.serializer.data

        self.assertEqual(data['price'], self.product_price_attributes['price'])

    def test_serializer_price_start_date_content(self):
        """Verifies the serializer contains the correct data in the 'price_start_date' field"""

        data = self.serializer.data

        self.assertEqual(data['price_start_date'],
                         self.product_price_attributes['price_start_date'])

    def test_serializer_price_end_date_content(self):
        """Verifies the serializer contains the correct data in the 'price_end_date' field"""

        data = self.serializer.data

        self.assertEqual(data['price_end_date'],
                         self.product_price_attributes['price_end_date'])
