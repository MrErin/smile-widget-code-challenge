from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from products.models import Product, GiftCard, ProductPrice
from products.views import PriceRequestView


class PriceRequestTest(APITestCase):

    def setUp(self):
        """builds dummy product, gift card, and price data for testing purposes"""

        self.client = APIClient()
        self.gift_card = GiftCard.objects.create(
            code='50OFF-FAKE', amount=5000, date_start='2018-10-01', date_end='2018-10-31')
        self.product = Product.objects.create(
            name='Widget', code='widget')
        self.product_price = ProductPrice.objects.create(
            code='widget', price='50000', price_start_date='2018-01-01', price_end_date='2018-12-31')
        # self.valid_3_kwargs = {'productCode': 'widget',
        #                        'date': '2018-10-02', 'giftCardCode': '50OFF-FAKE'}
        # self.valid_2_kwargs = {'productCode': 'widget', 'date': '2018-10-05'}
        # self.valid_3_response = self.client.post(
        #     reverse('get_price_with_gc'), self.valid_3_kwargs, format='json')
        # self.valid_2_response = self.client.post(
        #     reverse('get_price_without_gc'), self.valid_2_kwargs, format='json')

    def test_get_product(self):
        """Ensure we can pull a product from the API"""
        