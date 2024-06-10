from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to CosCalendars' API!"
    })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    
    # Access JWT_AUTH_COOKIE through settings.REST_AUTH
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_COOKIE'],
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],  # Access through settings.REST_AUTH
        secure=settings.REST_AUTH['JWT_AUTH_SECURE'],    # Access through settings.REST_AUTH
    )
    
    # Access JWT_AUTH_REFRESH_COOKIE through settings.REST_AUTH
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_REFRESH_COOKIE'],
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],  # Access through settings.REST_AUTH
        secure=settings.REST_AUTH['JWT_AUTH_SECURE'],    # Access through settings.REST_AUTH
    )

    return response
