from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import GiftCard
from products.serializers import GiftCardSerializer


def gift_card_list(request):
    """Lists all gift cards in the database"""
    gift_cards = GiftCard.objects.all()
    serializer = GiftCardSerializer(gift_cards, many=True)
    return JsonResponse(serializer.data, safe=False)


def gift_card_detail(request, pk):
    """Get details on a specific gift card"""

    try:
        gift_card = GiftCard.objects.get(pk=pk)
    except GiftCard.DoesNotExist:
        return HttpResponse(status=404)

    serializer = GiftCardSerializer(gift_card)
    return JsonResponse(serializer.data)
