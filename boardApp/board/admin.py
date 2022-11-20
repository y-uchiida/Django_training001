from django.contrib import admin

# 投稿データ用のモデルを読み込み
from .models import Post

# Register your models here.

admin.site.register(Post)
