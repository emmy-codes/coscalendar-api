from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from .models import CosExpense
from .serializers import CosExpenseSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q



class CosExpenseList(ListCreateAPIView):
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = CosExpense.objects.all()
        
        cosplay_name = self.kwargs.get("cosplay_name")
        if cosplay_name is not None:
            queryset = queryset.filter(Q(cosplayer=self.request.user) & Q(cosplay_name=cosplay_name))
        return queryset


class CosExpenseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosExpense.objects.all()
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
