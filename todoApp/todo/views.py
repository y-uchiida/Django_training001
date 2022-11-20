from django.shortcuts import render

# urlのルーティングを遅延解決する関数 reverse_lazyを読み込み
from django.urls import reverse_lazy

# Todoモデルを読み込み
from .models import TodoModel

# ListViewをよみこみ
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView

# Create your views here.

class TodoList(ListView):
    # リスト表示するモデルを指定
    model = TodoModel
    
    # 表示に利用するhtml を指定
    template_name: str = 'list.html'

class TodoDetail(DetailView):
    # リスト表示するモデルを指定
    model = TodoModel

    # 表示に利用するhtml を指定
    template_name: str = 'detail.html'

class TodoCreate(CreateView):
    # リスト表示するモデルを指定
    model = TodoModel

    # 表示に利用するhtml を指定
    template_name: str = 'create.html'
    
    # 画面上で操作させるフィールドをタプルで指定する
    fields = ('title', 'memo', 'priority', 'duedate')
    
    # データ作成後に遷移するURLを、urls.py のルーティングで指定されたname 属性から取得する
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    # リスト表示するモデルを指定
    model = TodoModel

    # 表示に利用するhtml を指定
    template_name: str = 'delete.html'
    
    # データ削除後に遷移するURLを、urls.py のルーティングで指定されたname 属性から取得する
    success_url = reverse_lazy('list')
    