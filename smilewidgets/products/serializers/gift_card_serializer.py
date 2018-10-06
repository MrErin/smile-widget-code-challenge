from rest_framework import serializers
from products.models import GiftCard


class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = ('code', 'amount', 'date_start', 'date_end')
