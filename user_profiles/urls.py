from django.urls import path
from user_profiles import views

urlpatterns = [
    # path("user_profiles/", views.UserProfileCreateOrUpdateView.as_view()),
    path("user_profiles/", views.UserProfileDetail.as_view())
]
