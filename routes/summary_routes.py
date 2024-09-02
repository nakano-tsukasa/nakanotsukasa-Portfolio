#====================パッケージ====================

from flask import Blueprint
from models import 

#====================Blueprint設定====================

summary_bp = Blueprint('summary', __name__)

#====================original要約文登録====================
#====================derived要約文作成====================
#====================derived要約文登録====================

@summary_bp.route('/')
def summary():
