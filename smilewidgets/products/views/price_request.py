import datetime
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import GiftCard, Product, ProductPrice


class PriceRequestView(APIView):
    """Retrieves the appropriate product price given a date, product code, and (optional) gift card code"""

    def get(self, request, *args, **kwargs):
        productCode = kwargs['productCode']
        date = kwargs['date']
        giftCardCode = kwargs.get('giftCardCode', '')

        data = {
            'productCode': '',
            'date': '',
            'giftCardCode': '',
            'productName': '',
            'productPrice': ''
        }

        # ensure the product is in the database
        if self.validate_product_code(productCode):
            data['productCode'] = productCode
        else:
            return Response('Product code not found.', status=400)

        # ensure the date is properly formatted
        if self.validate_date(date):
            data['date'] = date
        else:
            return Response('Enter a date in YYYY-MM-DD format.', status=400)

        # ensure the gift card is in the database and is valid
        if giftCardCode == '':
            pass
        elif self.validate_gift_card(giftCardCode, date):
            data['giftCardCode'] = giftCardCode
        else:
            return Response('Expired or invalid gift card code.', status=400)

        # grab the name of the product, because why not?
        data['productName'] = model_to_dict(
            Product.objects.get(code=productCode))['name']

        # calculate the price, including sales
        data['productPrice'] = self.calculate_price(
            productCode, date, giftCardCode)

        return Response(data)

    def validate_product_code(self, productCode):
        """Checks that the product code exists in both the Product and ProductPrice tables"""

        if Product.objects.filter(code=productCode).exists() and ProductPrice.objects.filter(code=productCode).exists:
            return True
        else:
            return False

    def validate_date(self, date):
        """Checks that the date is correctly formatted"""

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False

    def validate_gift_card(self, giftCardCode, date):
        """Checks that the gift card code is in the GiftCard table and that it is valid for the given date"""

        gift_card_start = model_to_dict(
            GiftCard.objects.get(code=giftCardCode))['date_start']
        gift_card_end = model_to_dict(
            GiftCard.objects.get(code=giftCardCode))['date_end']

        if GiftCard.objects.filter(code=giftCardCode).exists() and self.date_in_range(date, gift_card_start, gift_card_end):
            return True
        else:
            return False

    def date_in_range(self, check_date, range_start, range_end):
        """Validates that the checked date is inside the range of dates"""

        if str(range_start) <= check_date and str(range_end) >= check_date:
            return True
        else:
            return False

    def calculate_price(self, productCode, date, giftCardCode=''):
        """Calculates the product price based on the date and the (optional) offset of a gift card code"""

        price_calc = ''

        # find the product's price based on the date
        price_records_for_product = ProductPrice.objects.filter(
            code=productCode).values()

        for price_record in price_records_for_product:
            if self.date_in_range(date, price_record['price_start_date'], price_record['price_end_date']):
                price_calc = price_record['price']

        # subtract the gift card if available
        if giftCardCode == '':
            pass
        else:
            gift_card = model_to_dict(GiftCard.objects.get(code=giftCardCode))
            price_calc -= gift_card['amount']

        # ensure that the price can't fall below zero
        if price_calc <= 0:
            return '$0'
        else:
            return '${0:.2f}'.format(price_calc / 100)
