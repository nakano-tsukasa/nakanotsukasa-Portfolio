#====================パッケージ====================

from flask import Blueprint, request, redirect, render_template
from models import Summaries, Derived_summaries, db
from flask_login import login_required, current_user
from utils.chat_gpt import generate_summary_via_chatgpt

#====================Blueprint設定====================

summary_bp = Blueprint('summary', __name__)

#====================summarizer.html最新要約文取得====================



#====================original要約文登録====================
#====================derived要約文作成====================
#====================derived要約文登録====================

@summary_bp.route('/add_summary', methods=['POST'])
@login_required()
def add_summary():
    book_id = request.form.get['book_id']
    summary_text = request.form['newSummary']
    newSummary = Summaries(
        user_id = current_user.id,
        book_id = book_id,
        summary_text = summary_text

# book_idの取得未実装

    )
    db.session.add(newSummary)
    db.session.commit()


    latest_derived_summary = db.session.query(Derived_summaries.d_summary_text)\
    .filter(Derived_summaries.book_id == book_id)\
    .order_by(Derived_summaries.d_created_at.desc())\
    .first()
    latest_d_summary_text = latest_derived_summary.d_summary_text if latest_derived_summary else None

    combined_texts = f"{latest_d_summary_text}\n{summary_text}"
    ai_generated_summary = generate_summary_via_chatgpt(combined_texts)

    new_derived_summary = Derived_summaries(
        user_id = current_user.id,
        book_id = book_id,
        d_summary_text = ai_generated_summary
    )

    db.session.add(new_derived_summary)
    db.session.commit()

    return render_template('summarizer')
