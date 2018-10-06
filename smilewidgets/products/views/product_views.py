from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import Product
from products.serializers import ProductSerializer


def product_list(request):
    """Lists all products in the database"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


def product_detail(request, pk):
    """Get details on a specific product"""

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)
