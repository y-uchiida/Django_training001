from django.contrib import admin
from django.urls import path, include

# 設定ファイルの内容を参照するため、settingsを読み込み
from django.conf import settings

# 静的ファイルへのルーティングを設定するため、static を読み込み
from django.conf.urls.static import static

from .views import register_user
from .views import sign_in
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', register_user),
    path('auth/sign-in', sign_in),
    path('dashboard', dashboard),
] \
+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
