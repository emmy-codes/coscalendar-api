from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CosExpense
from .serializers import CosExpenseSerializer
from coscalendar_api.permissions import IsCosplayerOrReadOnly


class CosExpenseList(APIView):
    serializer_class = CosExpenseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        expenses = CosExpense.objects.all()  
        serializer = CosExpenseSerializer(
            expenses, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CosExpenseSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CosExpenseDetail(APIView):
    permission_classes = [IsCosplayerOrReadOnly]
    serializer_class = CosExpenseSerializer

    def get_object(self, pk):
        try:
            expense = CosExpense.objects.get(pk=pk)
            self.check_object_permissions(self.request, expense)
            return expense
        except CosExpense.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = CosExpenseSerializer(
            expense, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = CosExpenseSerializer(
            expense, data=request.data, context={"request": request}
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)