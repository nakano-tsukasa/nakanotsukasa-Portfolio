#====================パッケージ====================

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import Books, db
from flask_login import current_user, login_required

#====================Blueprint設定====================

book_register_bp = Blueprint('book_register', __name__)

#====================書籍登録用ルート====================

@book_register_bp.route('/', methods=['POST'])
@login_required
def register():
    book_name = request.form.get('bookTitle')
    g_id = request.form.get('bookGroup')
    author = request.form.get('author') or None
    published_date = request.form.get('publishedDate') or None

    user_id = current_user.id

    new_book = Books(user_id=user_id, book_name=book_name, g_id=g_id, author=author, published_date=published_date)
    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('main.book_list'))

#====================書籍グループ内情報取得用ルート====================

@book_register_bp.route('/get_group_info/<int:group_id>', methods=['GET'])
@login_required
def get_group_info(group_id):
    books = Books.query.filter_by(user_id=current_user.id).all()
    group_books = [book for book in books if book['g_id'] == group_id]

    return jsonify({"books": group_books})
