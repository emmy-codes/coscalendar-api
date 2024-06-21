from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly


class UserProfileList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer
    
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        user_profiles = user_profiles.filter(cosplayer=self.request.user)
        serializer = UserProfileSerializer(
            user_profiles, many=True, context={"request": request}
        )
        return Response(serializer.data)


class UserProfileDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        try:
            user_profile = UserProfile.objects.get(cosplayer=self.request.user)
            self.check_object_permissions(self.request, user_profile)
            return user_profile
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request):
        user_profile = UserProfile.objects.get(cosplayer=self.request.user)
        serializer = UserProfileSerializer(
            user_profile, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(cosplayer=self.request.user)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileCreateOrUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, serializer):
        # connects the new UserProfile with the currently logged-in user
        serializer.save(cosplayer=self.request.user) 

    def get_object(self):
        # get the UserProfile object for the currently logged-in user
        try:
            return UserProfile.objects.get(cosplayer=self.request.user)
        except UserProfile.DoesNotExist:
            raise Http404