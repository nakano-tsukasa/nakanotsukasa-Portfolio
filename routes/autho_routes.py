#====================パッケージ====================

from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User_profiles, db
from utils.token_utils import generate_verification_token, verify_verification_token
from utils.email_utils import  send_verification_email

from flask_login import login_user, logout_user

from models import User, Book_Groups

#====================Blueprint設定====================

auth_bp = Blueprint('auth', __name__)

#====================サインアップ用ルート====================

# ユーザー情報取得
# パスワードをハッシュ化
# 重複チェック
# 新規ユーザーの作成
# メール確認トークンの生成、メール送信

@auth_bp.route('/submitinfo', methods=['POST'])
def submitinfo():
    name = request.form['InputName']#formのnameを指定し値を取得する
    email = request.form['InputEmail']
    password = request.form['InputPassword']
    password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)#パスワードをハッシュ化する

    if User_profiles.query.filter_by(email=email).first():#メールはユニーク値なので、DBとの不一致をチェックする
        return "Email already exists!"

        # クエリを直接文字列で表現すると危険なので注意する（例
        # email_input = "example@example.com OR 1=1"  # 悪意のあるユーザーが入力した例
        # query = f"SELECT * FROM users WHERE email = '{email_input}'"
        # user = db.session.execute(query).first()

    new_user = User_profiles(name=name, email=email, password_hash=password_hash)

    db.session.add(new_user)#SQLAlchemyのセッションオブジェクトに、新しいレコードを追加する。セッションはトランザクションを制御している。
    db.session.commit()#セッション内の変更がデータベースに永続的に保存される。

    token = generate_verification_token(email)
    verification_url = url_for('auth.verify_email', token=token, _external=True)
    send_verification_email(email,verification_url)

    return redirect(url_for('main.confirmation_page'))

#====================メール確認用ルート====================

# トークンの検証
# 結果の表示

@auth_bp.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = verify_verification_token(token)#email_utils.pyよりデコードしてemailを返す関数
        user = User_profiles.query.filter_by(email=email).first()#.query.filter_byでSQLインジェクションを回避する
        if user:
            if not user.is_verified:# アカウントを有効化する
                user.is_verified = True
                db.session.commit()
                new_group = Book_Groups(g_name='others', user_id=user.id)# 本のグループにothersを作成する
                db.session.add(new_group)
                db.session.commit()
                message = "Email verified successfully! Please sign in below."
            else:
                message = "Account already verified."
        else:
            message = "Invalid verification token."
        return render_template('verify_email.html', message=message)
    except Exception as e:
        return render_template('verify_email.html', message=f"An error occurred: {e}")

#====================サインイン用ルート====================

# ユーザー情報取得
# パスワードの一致を確認
# login_user関数で、セッションにユーザー情報を保存

@auth_bp.route('/signin_post', methods=['POST'])
def signin_post():
    email = request.form.get('signinEmail')
    password = request.form.get('signinPassword')

    user = User_profiles.query.filter_by(email=email).first()#emailカラムが一致する行を取得する

    if user and check_password_hash(user.password_hash, password):
        if user.is_verified:
            login_user(User(user.id, user.name))# ユーザーのIDがセッションに保存され、アプリケーション全体でユーザーの状態を認識できるようになる
            return redirect(url_for('main.account'))
        else:
            flash('Your account is not verified. Please check your email for verification.', 'warning')
            return redirect(url_for('main.user_signin'))
    else:
        flash('Invalid email or password.', 'danger')
        return redirect(url_for('main.user_signin'))
    
#====================サインアウト用ルート====================

# logout_user関数を使って、ログアウト、ホームをリダイレクト。

@auth_bp.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('main.index'))