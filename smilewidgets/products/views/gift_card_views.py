from rest_framework import viewsets
from products.models import GiftCard
from products.serializers import GiftCardSerializer


class GiftCardViewSet(viewsets.ModelViewSet):
    """Viewset for listing or retrieving Gift Card Codes"""

    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
