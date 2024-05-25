from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CosPlan, Cosplay
from .serializers import CosPlanSerializer
from django.contrib.auth.models import User
from coscalendar_api.permissions import IsCosplayerOrReadOnly


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
        serializer = CosPlanSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(cosplayer=request.user)  # Associate with the logged-in User directly
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CosPlanDetail(APIView):
    permission_classes = [IsCosplayerOrReadOnly]
    serializer_class = CosPlanSerializer
    
    def get_object(self, pk):
        try:
            cosplan = CosPlan.objects.get(pk=pk)
            self.check_object_permissions(self.request, cosplan)
            return cosplan
        except CosPlan.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        cosplan = self.get_object(pk)
        serializer = CosPlanSerializer(
            cosplan, context={"request": request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        cosplan = self.get_object(pk)
        serializer = CosPlanSerializer(
            cosplan, data=request.data, context={"request": request}
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cosplan = self.get_object(pk)
        cosplan.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )