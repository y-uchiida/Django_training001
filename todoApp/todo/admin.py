from django.contrib import admin

# 作成したTodoモデルをロードする
from .models import TodoModel

# Register your models here.

# 管理サイトに、todoモデルを表示する
admin.site.register(TodoModel)
