"""helloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# views から読み込み
from .views import hello_world_function
from .views import hello_world_class

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world_function),
    path('hello-world-class/', hello_world_class.as_view()),
    
    # helloworld_app に処理を引き継ぐ
    path('hello-app', include('helloworld_app.urls'))
]
