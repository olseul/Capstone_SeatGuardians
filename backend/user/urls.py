from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from user.views import (
    UserRetrieveAPIView,
    UserDestoryAPIView,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("user/destroy/", UserDestoryAPIView.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("<int:id>/", UserRetrieveAPIView.as_view())
]
