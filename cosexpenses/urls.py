from django.urls import path
from cosexpenses import views

urlpatterns = [
    path("expenses/", views.CosExpenseList.as_view()),
    path("expenses/<int:pk>/", views.CosExpenseDetail.as_view())
]