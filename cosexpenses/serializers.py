from rest_framework import serializers
from .models import CosExpense


class CosExpenseSerializer(serializers.ModelSerializer):
    # will show cosplay name instead of the id
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")

    class Meta:
        model = CosExpense
        fields = [
            "id",
            "cosplayer",
            "item_name",
            "quantity",
            "unit_price",
            "product_link",
        ]
