from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import User_profiles, db
from utils.token_utils import generate_verification_token, verify_verification_token
from utils.email_utils import  send_verification_email

auth_bp = Blueprint('auth', __name__)

#ユーザー情報送信ポイント
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


#ユーザー認証完了ページ
@auth_bp.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = verify_verification_token(token)#email_utils.pyよりデコードしてemailを返す関数
        user = User_profiles.query.filter_by(email=email).first()#.query.filter_byでSQLインジェクションを回避する

        if user:
            # アカウントの有効化などの処理
            return render_template('verify_email.html', message="Email verified successfully!")
        else:
            return render_template('verify_email.html', message="Invalid verification token.")
    except Exception as e:
        return render_template('verify_email.html', message=f"An error occurred: {e}")
