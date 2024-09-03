#====================パッケージ====================

from flask import Blueprint, request, redirect, url_for
from models import Summaries, Derived_summaries, db
from flask_login import login_required, current_user
from utils.chat_gpt import generate_summary_via_chatgpt

#====================Blueprint設定====================

summary_bp = Blueprint('summary', __name__)

#====================original要約文登録====================
#====================derived要約文作成====================
#====================derived要約文登録====================

@summary_bp.route('/add_summary', methods=['POST'])
@login_required
def add_summary():
    book_id = request.form.get('book_id')
    book_name = request.form.get('book_name')
    summary_text = request.form.get('newSummary')
    newSummary = Summaries(
        user_id = current_user.id,
        book_id = book_id,
        summary_text = summary_text

# book_idの取得未実装

    )
    db.session.add(newSummary)
    db.session.commit()

    latest_derived_summary = Derived_summaries.query.filter(
        Derived_summaries.book_id == book_id, 
        Derived_summaries.user_id == current_user.id
    ).order_by(Derived_summaries.d_created_at.desc()).first()
    latest_d_summary_text = latest_derived_summary.d_summary_text if latest_derived_summary else None

    if latest_d_summary_text:
        ai_generated_summary = generate_summary_via_chatgpt(latest_d_summary_text,summary_text)
    else:
        ai_generated_summary = summary_text

    new_derived_summary = Derived_summaries(
        user_id = current_user.id,
        book_id = book_id,
        d_summary_text = ai_generated_summary
    )

    db.session.add(new_derived_summary)
    db.session.commit()

    return redirect(url_for('main.summarizer', book_id=book_id, book_name=book_name))
