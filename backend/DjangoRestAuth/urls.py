
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from DjangoRestAuth.views import ModsView, register

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to obtain a new access and refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Submit your refresh token to this path to obtain a new access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Return 'Mods' model objects
    path('mods/', ModsView.as_view(), name='mods_view'),
    # Register a new user
    path('register/', register, name='register_view'),
]
