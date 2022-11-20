from django.contrib import admin
from django.urls import path, include

from .views import TodoList
from .views import TodoDetail
from .views import TodoCreate
from .views import TodoDelete
from .views import TodoUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('list/', TodoList.as_view(), name='list'),
    
    # int型でpkを指定して、個別のデータをとる
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    
    # Todo新規作成用のviewを追加
    path('create/', TodoCreate.as_view(), name='create'),

    # Todo削除用のviewを追加
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),

    # Todo編集用のviewを追加
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
