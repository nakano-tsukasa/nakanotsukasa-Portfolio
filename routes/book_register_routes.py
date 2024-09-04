#====================パッケージ====================

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Books, db
from flask_login import current_user, login_required

#====================Blueprint設定====================

book_register_bp = Blueprint('book_register', __name__)

#====================書籍登録用ルート====================

@book_register_bp.route('/', methods=['POST'])
def register():
    book_name = request.form.get('bookTitle')
    author = request.form.get('author') or None
    published_date = request.form.get('publishedDate') or None

    user_id = current_user.id

    new_book = Books(user_id=user_id, book_name=book_name, author=author, published_date=published_date)
    db.session.add(new_book)
    db.session.commit()

    flash('Book successfully registerd!')
    return redirect(url_for('main.book_list'))