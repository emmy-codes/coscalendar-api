from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import CosPlan
from .serializers import CosPlanSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import request
from django.db.models import Q


class CosPlanList(ListCreateAPIView):
    queryset = CosPlan.objects.all().order_by("due_date")
    serializer_class = CosPlanSerializer
    permission_classes = [IsCosplayerOrReadOnly]
    pagination_class = PageNumberPagination
    
    # customized creation logic
    def perform_create(self, serializer):
        cosplayer = self.request.user
        if not cosplayer.is_authenticated:
            raise ValidationError(
                "You must be logged in to create a cosplan."
            )
        
        try:
            serializer.save(cosplayer=cosplayer)
        # for catching errors with user not being logged in
        except ValidationError as err:
            return Response(err.detail, status=status.HTTP_400_BAD_REQUEST)
        # for catching unexpected errors
        except Exception as e:
            print(f"Error creating your CosPlan: {e}")
            return Response(
                {"error": "An error occurred while creating your CosPlan."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

class CosPlanListByDateRange(ListCreateAPIView):
    def get_queryset(self):
        return CosPlan.objects.filter(Q(cosplayer=self.request.user), due_date__range=[self.request.query_params.get("startDate"), self.request.query_params.get("endDate")]).order_by("due_date")
    serializer_class = CosPlanSerializer
    permission_classes = [IsCosplayerOrReadOnly]


class CosPlanDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosPlan.objects.all()
    serializer_class = CosPlanSerializer
    permission_classes = [IsCosplayerOrReadOnly]
