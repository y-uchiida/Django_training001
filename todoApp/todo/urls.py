from django.contrib import admin
from django.urls import path, include

from .views import TodoList

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('list/', TodoList.as_view())
]
