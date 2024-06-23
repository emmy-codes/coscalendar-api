from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # noqa
from .models import CosExpense
from .serializers import CosExpenseSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from cosplans.models import CosPlan
from rest_framework import status



class CosExpenseList(ListCreateAPIView):
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = CosExpense.objects.all()
        
        queryset = queryset.filter(Q(cosplan=self.request.query_params.get("cosplan_id")))
        return queryset
    
    def perform_create(self, serializer):
        # Get the authenticated user
        cosplayer = self.request.user
    
        # get the cosplan record based on the cosplan_id sent on the request
        cosplan = CosPlan.objects.get(id=self.request.data.get('cosplan_id'))

        # Check if the user is authenticated
        if not cosplayer.is_authenticated:
            raise ValidationError("Authentication credentials were not provided.")

        # Save the expense with the authenticated user as the cosplayer
        serializer.save(cosplayer=cosplayer, cosplan=cosplan)
        
    def delete(self, request, pk):
        """
        Delete a cosplayer's expense by its primary key
        Add "cosplans/expenses/<int:pk>/" on cosplans/urls.py pointing to this view
        """

        try:
            # Fetch the CosExpense using the provided ID
            expense = CosExpense.objects.get(pk=pk)
        except CosExpense.DoesNotExist:
            return Response(
                {"error": "Expense not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if the user is the owner
        if expense.cosplayer != request.user:
            return Response(
                {"error": "You don't have permission to delete this expense."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Delete the expense
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CosExpenseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CosExpense.objects.all()
    serializer_class = CosExpenseSerializer
    permission_classes = [IsCosplayerOrReadOnly]
