from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_image = serializers.ReadOnlyField(source="user_profile.profile_image.url")
    profile_id = serializers.ReadOnlyField(source="user_profile.id")
    

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id", "profile_image"
        )