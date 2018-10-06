from rest_framework import serializers
from products.models import ProductPrice


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('code', 'price', 'price_start_date', 'price_end_date')
