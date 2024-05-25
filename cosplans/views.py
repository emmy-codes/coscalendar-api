from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CosPlan, Cosplay
from user_profiles.models import UserProfile
from .serializers import CosPlanSerializer
from django.contrib.auth.models import User


class CosPlanList(APIView):
    serializer_class = CosPlanSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        cosplans = CosPlan.objects.all()
        serializer = CosPlanSerializer(
            cosplans, many=True, context={"request": request}
        ) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CosPlanSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(cosplayer=request.user)  # Associate with the logged-in User directly

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)