from rest_framework import serializers


class PriceRequestSerializer(serializers.Serializer):
    productCode = serializers.CharField(max_length=10),
    productName = serializers.CharField(max_length=25),
    date = serializers.DateField(),
    giftCardCode = serializers.CharField(max_length=30)
    productPrice = serializers.CharField(max_length=30)
