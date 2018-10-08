from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers import PriceRequestSerializer


class PriceRequestView(APIView):
    """Retrieves the appropriate product price given a date, product code, and (optional) gift card code"""

    def get(self, request, *args, **kwargs):
        productCode = kwargs['productCode']
        date = kwargs['date']
        giftCardCode = kwargs.get('giftCardCode', '')

        data = {
            'productCode': productCode,
            'date': date,
            'giftCardCode': giftCardCode
            # 'productName': productName,
            # 'productPrice': productPrice

        }

        return Response(data)
