from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)# Blueprint名、呼出しはmain.indexなどとする。Blueprint名.関数名

@main_bp.route('/')
def index():
    return render_template('index.html')

#ユーザーのサインイン用ページ
@main_bp.route('/user_signin' ,methods=['GET','POST'])
def user_signin():
    return render_template('user_signin.html')

#ユーザーのサインアップ用ページ
@main_bp.route('/user_signup')
def user_signup():
    return render_template('user_signup.html')

#ユーザーへの認証メール送信通知ページ
@main_bp.route('/confirmation_page')
def confirmation_page():
    return render_template('confirmation_page.html')

#アカウントページ
@main_bp.route('/account')
def account():
    return render_template('account.html')