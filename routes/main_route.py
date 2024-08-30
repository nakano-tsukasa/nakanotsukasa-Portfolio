from flask import Blueprint, render_template
from flask_login import current_user, login_required

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
@login_required
def account():
    return render_template('account.html')

@main_bp.route('/summarizer')
@login_required
def summarizer():
    return render_template('summarizer.html')

@main_bp.route('/book_list')
@login_required
def book_list():
    return render_template('book_list.html')