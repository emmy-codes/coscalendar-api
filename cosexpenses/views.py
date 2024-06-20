from django.forms import ValidationError
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
        
        # queryset = queryset.filter(Q(cosplayer=self.request.user) & Q(cosplan=self.request.query_params.get("cosplan_id")))
        return queryset
    
    def perform_create(self, serializer):
        # Get the authenticated user
        cosplayer = self.request.user

        # Check if the user is authenticated
        if not cosplayer.is_authenticated:
            raise ValidationError("Authentication credentials were not provided.")

        # Save the expense with the authenticated user as the cosplayer
        serializer.save(cosplayer=cosplayer)


class CosExpenseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosExpense.objects.all()
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
