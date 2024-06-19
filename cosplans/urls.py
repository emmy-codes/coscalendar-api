from django.urls import path
from cosplans import views

urlpatterns = [
    path("cosplans/", views.CosPlanList.as_view()),
    path("cosplansbyDateRange/", views.CosPlanListByDateRange.as_view()),
    path("cosplans/<int:pk>/", views.CosPlanDetail.as_view())
]
