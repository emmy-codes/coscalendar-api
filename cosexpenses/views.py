from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from .models import CosExpense
from .serializers import CosExpenseSerializer, CosExpenseDetailSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly
from rest_framework.pagination import PageNumberPagination


class CosExpenseList(ListCreateAPIView):
    queryset = CosExpense.objects.all()
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
    pagination_class = PageNumberPagination


class CosExpenseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosExpense.objects.all()
    serializer_class = CosExpenseDetailSerializer
    permission_classes = [IsCosplayerOrReadOnly]
