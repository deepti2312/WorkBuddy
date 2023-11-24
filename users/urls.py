from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import (
    LoginView,
    LogoutView,
    RegisterView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
