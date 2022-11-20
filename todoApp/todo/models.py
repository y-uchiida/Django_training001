from django.db import models

# Create your models here.

# 優先度設定用のタプルを作成
PRIORITIES = ('high', 'high'), ('normal', 'normal'), ('low', 'low')

# todo のモデルを作成する
class TodoModel(models.Model):
    # カラム名と型を定義
    title = models.CharField(max_length=100)
    memo = models.TextField()
    
    priority = models.CharField(
        max_length=50,
        # priority カラムに入るべき値をタプルで指定
        choices=PRIORITIES
    )
    
    # 締め切り日を設定するカラム
    duedate = models.DateField()

    def __str__(self):
        return self.title
