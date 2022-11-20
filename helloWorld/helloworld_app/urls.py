from django.urls import path
from .views import hello_world_app_view

urlpatterns = [
    path('/', hello_world_app_view)
]
