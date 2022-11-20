from django.contrib import admin
from django.urls import path, include

from .views import TodoList
from .views import TodoDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('list/', TodoList.as_view()),
    
    # int型でpkを指定して、個別のデータをとる
    path('detail/<int:pk>', TodoDetail.as_view())
]
