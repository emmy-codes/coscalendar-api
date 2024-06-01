from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from .models import CosPlan
from .serializers import CosPlanSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class CosPlanList(ListCreateAPIView):
    queryset = CosPlan.objects.all().order_by('due_date')
    serializer_class = CosPlanSerializer
    permission_classes = [IsCosplayerOrReadOnly]
    pagination_class = PageNumberPagination


class CosPlanDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosPlan.objects.all()
    serializer_class = CosPlanSerializer
    permission_classes = [IsCosplayerOrReadOnly]