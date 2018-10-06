from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import ProductPrice
from products.serializers import ProductPriceSerializer


def product_price_list(request):
    """Lists all product prices in the database"""
    product_prices = ProductPrice.objects.all()
    serializer = ProductPriceSerializer(product_prices, many=True)
    return JsonResponse(serializer.data, safe=False)


def product_price_detail(request, pk):
    """Get details on a specific product price"""

    try:
        product_price = ProductPrice.objects.get(pk=pk)
    except ProductPrice.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductPriceSerializer(product_price)
    return JsonResponse(serializer.data)
