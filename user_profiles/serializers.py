from rest_framework import serializers
from .models import UserProfile

 
class UserProfileSerializer(serializers.ModelSerializer):
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    # read only serializer field
    is_cosplayer = serializers.SerializerMethodField()
    
    def get_is_cosplayer(self, obj):
       request = self.context["request"]
       return request.user == obj.cosplayer 
    
    class Meta:
        model = UserProfile
        fields = "__all__"