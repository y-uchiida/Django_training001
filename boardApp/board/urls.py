from django.contrib import admin
from django.urls import path, include

from .views import register_user
from .views import sign_in
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', register_user),
    path('auth/sign-in', sign_in),
    path('dashboard', dashboard),
]
