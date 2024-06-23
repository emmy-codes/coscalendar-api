from rest_framework import serializers
from .models import CosPlan


class CosPlanSerializer(serializers.ModelSerializer):
    # displays username instead of ID
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")

    def get_is_cosplayer(self, obj):
        request = self.context["request"]
        return request.user == obj.cosplayer

    class Meta:
        model = CosPlan
        fields = [
            "id",
            "cosplayer",  # displays username instead of ID
            "cosplay",
            "cosplan_task",
            "due_date",
            "cosplan_details"
        ]
