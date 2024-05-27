from rest_framework import serializers
from .models import CosExpense


class CosExpenseSerializer(serializers.ModelSerializer):
    # will show cosplay name instead of the id
    cosplay = serializers.StringRelatedField()
    # calc / display total cost (quantity * unit_price)
    total_cost = serializers.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        model = CosExpense
        fields = "__all__"
        read_only_fields = ["total_cost"]
    
    def get_total_cost(eslf, obj):
        return obj.total_cost