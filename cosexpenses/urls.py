from django.urls import path
from .views import CosExpenseList, CosExpenseDetail

urlpatterns = [
    path("expenses/", CosExpenseList.as_view()),
    path("expenses/<int:pk>/", CosExpenseDetail.as_view())
]