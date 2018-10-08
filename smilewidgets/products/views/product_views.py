from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Viewset for listing or retrieving Products"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
