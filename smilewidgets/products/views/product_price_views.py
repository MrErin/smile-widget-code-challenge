from rest_framework import viewsets
from products.models import ProductPrice
from products.serializers import ProductPriceSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    """Viewset for listing or retrieving product prices"""

    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
