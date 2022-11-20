from django.contrib import admin
from django.urls import path, include

from .views import TodoList
from .views import TodoDetail
from .views import TodoCreate
from .views import TodoDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('list/', TodoList.as_view(), name='list'),
    
    # int型でpkを指定して、個別のデータをとる
    path('detail/<int:pk>', TodoDetail.as_view()),
    
    # Todo新規作成用のviewを追加
    path('create/', TodoCreate.as_view(), name='create'),

    # Todo削除用のviewを追加
    path('delete/<int:pk>', TodoDelete.as_view()),
]
