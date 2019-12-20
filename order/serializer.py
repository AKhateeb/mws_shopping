from rest_framework import serializers
from .models import Order, OrderDetails


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = "__all__"