from rest_framework import serializers
from .models import Cosplay, CosPlan


class CosPlanSerializer(serializers.ModelSerializer):
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    is_cosplayer = serializers.SerializerMethodField()
    user_profile_id = serializers.ReadOnlyField(source="cosplayer.user_profile.id") # noqa
    
    def get_is_cosplayer(self, obj):
        request = self.context["request"]
        return request.user == obj.cosplayer
    
    class Meta:
        model = CosPlan
        fields = "__all__"