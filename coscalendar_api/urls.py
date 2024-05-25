from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import urlpatterns as drf_urls
from user_profiles import views as user_profiles_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Include user_profile URLs directly
    path("user_profiles/", user_profiles_views.UserProfileList.as_view()),
    path("user_profiles/<int:pk>/", user_profiles_views.UserProfileDetail.as_view()),
    path('', include('cosplans.urls')),
]
