from models import Summaries
from flask_login import current_user
from sqlalchemy import func

def book_list_sort(user_books):

    latest_updates = {}
    for book in user_books:
        latest_summary = (Summaries.query
                            .filter_by(user_id=current_user.id, book_id=book.book_id)
                            .order_by(Summaries.updated_at.desc())
                            .first())
        
        if latest_summary:
            latest_updates[book.book_id] = latest_summary.updated_at
        else:
            latest_updates[book.book_id] = book.b_updated_at

    sorted_user_books = sorted(user_books, key=lambda book: latest_updates.get(book.book_id, func.now()), reverse=True)

    return sorted_user_books