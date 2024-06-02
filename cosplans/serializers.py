from rest_framework import serializers
from .models import CosPlan, Cosplay


class CosPlanSerializer(serializers.ModelSerializer):
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    is_cosplayer = serializers.SerializerMethodField()
    cosplay = serializers.PrimaryKeyRelatedField(queryset=Cosplay.objects.all(), default=serializers.CurrentUserDefault())  # noqa


    def get_is_cosplayer(self, obj):
        request = self.context["request"]
        return request.user == obj.cosplayer

    class Meta:
        model = CosPlan
        fields = "__all__"


class CosPlanDetailSerializer(CosPlanSerializer):
    cosplay = serializers.StringRelatedField(read_only=True)
