#====================パッケージ====================

from flask import Blueprint, render_template
from flask_login import current_user, login_required

#====================Blueprint設定====================

main_bp = Blueprint('main', __name__)# Blueprint名、呼出しはmain.indexなどとする。Blueprint名.関数名

#====================Model設定====================

from models import Books

#====================route設定====================

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

#要約ページ
@main_bp.route('/summarizer')
@login_required
def summarizer():
    return render_template('summarizer.html')

#書籍登録ページ
@main_bp.route('/registration')
@login_required
def registration():
    return render_template('registration.html')

#書籍一覧ページ
@main_bp.route('/book_list')
@login_required
def book_list():
    books = Books.query.all()
    return render_template('book_list.html', books=books)