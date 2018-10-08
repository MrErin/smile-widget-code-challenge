from django.test import TestCase
from products.models import Product
from products.serializers import ProductSerializer


class ProductTest(TestCase):
    """Test cases for the Product class"""

    def setUp(self):
        """Test case setup"""

        self.product_attributes = {
            'name': 'Big Widget',
            'code': 'big_widget'
        }

        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_model_string_representation(self):
        """Verifies the output of the str method"""

        self.assertEqual(str(self.product), 'Big Widget - big_widget')

    def test_serializer_contains_expected_fields(self):
        """Verifies that the serializer contains all of the fields it should and none of the fields it shouldn't"""

        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), ['name', 'code'])

    def test_serializer_name_content(self):
        """Verifies the serializer contains the correct data in the 'name' field"""

        data = self.serializer.data

        self.assertEqual(data['name'], self.product_attributes['name'])

    def test_serializer_code_content(self):
        """Verifies the serializer contains the correct data in the 'code' field"""

        data = self.serializer.data

        self.assertEqual(data['code'], self.product_attributes['code'])
