# HttpResponse を読み込み
from django.http import HttpResponse

# クラスベースViewを取得
from django.views.generic import TemplateView

def hello_world_function(req):
    return HttpResponse('hello world')

# TemplateViewを継承して設定を行う
class hello_world_class(TemplateView):
    template_name:str = 'hello.html'
