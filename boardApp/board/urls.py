from django.contrib import admin
from django.urls import path, include

# 設定ファイルの内容を参照するため、settingsを読み込み
from django.conf import settings

# 静的ファイルへのルーティングを設定するため、static を読み込み
from django.conf.urls.static import static

from .views import register_user
from .views import sign_in
from .views import sign_out
from .views import dashboard
from .views import show_post
from .views import increase_like
from .views import mark_read
from .views import PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', register_user),
    path('auth/sign-in', sign_in, name='sign-in'),
    path('auth/sign-out', sign_out, name='sign-out'),
    path('dashboard', dashboard, name='dashboard'),
    path('post/<int:pk>', show_post, name='show_post'),
    path('post/<int:pk>/increase_like', increase_like, name='increase_like'),
    path('post/<int:pk>/mark_read', mark_read, name='mark_read'),
    path('post/create', PostCreateView.as_view(), name='create_post'),
] \
+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
