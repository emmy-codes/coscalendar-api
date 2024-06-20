from rest_framework import serializers
from .models import CosExpense


class CosExpenseSerializer(serializers.ModelSerializer):
    # will show cosplay name instead of the id
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    # calc / display total cost (quantity * unit_price)
    total_cost = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = CosExpense
        fields = [
            "id",
            "cosplayer",
            "cosplay_name",
            "item_name",
            "quantity",
            "unit_price",
            "product_link",
            "total_cost",
        ]
        read_only_fields = ["total_cost"]

    def get_total_cost(eslf, obj):
        return obj.total_cost