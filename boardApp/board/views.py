from django.shortcuts import render

# ユーザーの重複登録時のエラーを読み込みし、ハンドリングに利用する
from django.db import IntegrityError

from django.contrib.auth.models import User

# Create your views here.

# ユーザー登録画面と登録の処理
def register_user(req):
    if req.method == 'POST':
        # POST メソッドでリクエストされた場合、Userモデルにデータを追加する
        username = req.POST['username']
        password = req.POST['password']
        
        if not username or not password:
            # 内容が入力されていない場合
            return render(req, 'register_user.html', {'error': 'ユーザー名、パスワードを入力してください'})

        try:
            # User クラス経由でcreate_user() メソッドを呼び出す
            User.objects.create_user(username, '', password)
        except IntegrityError:
            # エラー情報を持たせて、ユーザー登録画面に戻す
            return render(req, 'register_user.html', {'error': '登録済みのユーザーです'})
        except ValueError:
            return render(req, 'register_user.html', {'error': '入力内容が正しくありません'})
            

    # render() で画面描画のレスポンスを返す
    # 1. リクエストオブジェクト, 2. テンプレートのhtml, 3. 描画に用いるデータ
    return render(req, 'register_user.html', {})
