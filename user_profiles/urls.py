from django.urls import path
from user_profiles import views

urlpatterns = [
    path("user_profiles/", views.UserProfileList.as_view()),
    path("user_profiles/<int:pk>/", views.UserProfileDetail.as_view())
]
