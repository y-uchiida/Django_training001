from django.contrib import admin
from django.urls import path, include

from .views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', register_user),
]
