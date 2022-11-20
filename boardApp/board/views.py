from django.shortcuts import render

# Create your views here.

# ユーザー登録画面と登録の処理
def register_user(req):
    # render() で画面描画のレスポンスを返す
    # 1. リクエストオブジェクト, 2. テンプレートのhtml, 3. 描画に用いるデータ
    return render(req, 'register_user.html', {})
