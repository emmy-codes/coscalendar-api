from rest_framework import serializers
from .models import UserProfile

 
class UserProfileSerializer(serializers.ModelSerializer):
    cosplayer = serializers.ReadOnlyField(source="cosplayer.username")
    
    class Meta:
        model = UserProfile
        fields = "__all__"