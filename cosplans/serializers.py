from rest_framework import serializers
from .models import CosPlan, Cosplay


class CosPlanSerializer(serializers.ModelSerializer):
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    is_cosplayer = serializers.SerializerMethodField()
    cosplay = serializers.PrimaryKeyRelatedField(queryset=Cosplay.objects.all(), default=serializers.CurrentUserDefault()) # noqa
    
    
    """
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image size is larger than 2MB!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width is larger than 4096px"
            )
        if value.image.height > 4096:
            raise seralizers.ValidationError(
                "Image height is larger than 4096px"
            )
        return value
    """       
    
    def get_is_cosplayer(self, obj):
        request = self.context["request"]
        return request.user == obj.cosplayer
    
    class Meta:
        model = CosPlan
        fields = "__all__"