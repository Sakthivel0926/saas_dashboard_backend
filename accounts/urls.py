from django.urls import path
from .views import UserListCreateView, UserDetailView
from .views import SignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("signup/", SignupView.as_view(), name="signup"),

    path("login/", TokenObtainPairView.as_view(), name="login"),

    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
]