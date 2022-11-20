from django.shortcuts import render
from django.shortcuts import redirect

# ユーザーの重複登録時のエラーを読み込みし、ハンドリングに利用する
from django.db import IntegrityError

from django.contrib.auth.models import User

# 指定のユーザー情報に当てはまるユーザーがあるかを検証するメソッドを読み込み
from django.contrib.auth import authenticate

# 指定のユーザーオブジェクトでログインするメソッドを読み込み
from django.contrib.auth import login

# ユーザーをログアウトさせるメソッドを読み込み
from django.contrib.auth import logout

# 認証していなければサインイン画面に遷移させるデコレータを読み込み
from django.contrib.auth.decorators import login_required

from .models import Post

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
            # ユーザー追加に成功すると、そのユーザーのオブジェクトを返す
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            # エラー情報を持たせて、ユーザー登録画面に戻す
            return render(req, 'register_user.html', {'error': '登録済みのユーザーです'})
        except ValueError:
            return render(req, 'register_user.html', {'error': '入力内容が正しくありません'})
        
        try:
            # 作成したユーザーでログイン
            login(req, user)
            return redirect('/dashboard')
        except:
            return render(req, 'sign_in.html', {'error': 'サインイン処理に失敗しました'})
            
    # render() で画面描画のレスポンスを返す
    # 1. リクエストオブジェクト, 2. テンプレートのhtml, 3. 描画に用いるデータ
    return render(req, 'register_user.html', {})

def sign_in(req):
    if req.method == 'POST':
        # POST メソッドでリクエストされた場合、入力された内容でサインインを試行する
        username = req.POST['username']
        password = req.POST['password']
        # authenticate() からユーザーオブジェクトが返ってくれば、ログインできる
        user = authenticate(req, username=username, password=password)
        
        # 結果がNone なら入力内容が間違っている
        if user is None:
            return render(req, 'sign_in.html', {'error': 'ユーザー名またはパスワードが正しくありません'})
        
        try:
            login(req, user)
            return redirect('/dashboard')
        except:
            return render(req, 'sign_in.html', {'error': 'サインイン処理に失敗しました'})
    
    # render() で画面描画のレスポンスを返す
    # 1. リクエストオブジェクト, 2. テンプレートのhtml, 3. 描画に用いるデータ
    return render(req, 'sign_in.html', {})

def sign_out(req):
    logout(req)
    return redirect('sign-in')

# login_required で、ログインしていなければ表示できないようにする
@login_required
def dashboard(req):
    # 投稿の全データを取得
    posts = Post.objects.all()
    return render(req, 'dashboard.html', {'posts': posts})
