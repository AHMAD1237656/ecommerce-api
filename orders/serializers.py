from rest_framework import serializers

from .models import Order, OrderItem

from .models import Order, OrderItem, Payment


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "quantity",
            "price",
        ]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "customer",
            "status",
            "total_amount",
            "shipping_address",
            "items",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "order_number",
            "status",
            "total_amount",
            "created_at",
            "updated_at",
        ]
    
    
class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"

        read_only_fields = [
            "transaction_id",
            "status",
            "created_at",
            "updated_at",
        ]