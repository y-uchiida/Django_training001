from django.db import models

# Create your models here.

# todo のモデルを作成する
class TodoModel(models.Model):
    # カラム名と型を定義
    title = models.CharField(max_length=100)
    memo = models.TextField()
