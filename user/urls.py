from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView) 

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', TokenObtainPairView.as_view()),
    path('sign-in/refresh', TokenRefreshView.as_view()),
]
