from django.shortcuts import render

# Todoモデルを読み込み
from .models import TodoModel

# ListViewをよみこみ
from django.views.generic.list import ListView

# Create your views here.

class TodoList(ListView):
    # リスト表示するモデルを指定
    model = TodoModel
    
    # 表示に利用するhtml を指定
    template_name: str = 'list.html'
