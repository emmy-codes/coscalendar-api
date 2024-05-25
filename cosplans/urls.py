from django.urls import path
from cosplans import views

urlpatterns = [
    path("cosplans/", views.CosPlanList.as_view()),
]