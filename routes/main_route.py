#====================パッケージ====================

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from models import Books, Derived_summaries

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
    user_books = Books.query.filter_by(user_id=current_user.id).all()
    return render_template('account.html', books=user_books)

#要約ページ
@main_bp.route('/summarizer')
@login_required
def summarizer():
    book_id = request.args.get('book_id')
    book_name = request.args.get('book_name')
    # 最新の d_summary_text を取得
    latest_summary = Derived_summaries.query.filter_by(
        book_id=book_id, user_id=current_user.id
    ).order_by(Derived_summaries.d_created_at.desc()).first()
    return render_template('summarizer.html',
                           book_id=book_id,
                           book_name=book_name,
                           latest_summary=latest_summary
    )

#書籍登録ページ
@main_bp.route('/registration')
@login_required
def registration():
    return render_template('registration.html')

#書籍一覧ページ
@main_bp.route('/book_list')
@login_required
def book_list():
    user_books = Books.query.filter_by(user_id=current_user.id).all()
    return render_template('book_list.html', books=user_books)