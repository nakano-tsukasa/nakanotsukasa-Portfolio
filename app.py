#====================パッケージインストール====================

from flask import Flask#Webサーバ構築用パッケージ
from models import db#データベースのモデル（ORM）の定義を取り込み
import os

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User, User_profiles

from routes.autho_routes import auth_bp
from routes.main_route import main_bp
from routes.book_register_routes import book_register_bp
from routes.summary_routes import summary_bp

#====================Flask app設定と初期化、データベース接続の初期化====================

DBSERVER_URI = os.getenv('DBSERVER_URI')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)#インスタンスを作成
app.config['SQLALCHEMY_DATABASE_URI'] = DBSERVER_URI#あとでadminからuser用のPOST専用DBユーザーに変更する
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#オブジェクトのモディファイを無効にする
app.config['SECRET_KEY'] = SECRET_KEY# セッション管理やCSRF保護（未実装）に使用する

db.init_app(app)# dbオブジェクトをFlask appと紐づける。データベース接続の初期化。


#--------------------Flask-Loginの設定--------------------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.user_signin'# 未ログイン時のリダイレクト先

@login_manager.user_loader# ユーザーの読み込み
def load_user(user_id):
    user_data = User_profiles.query.get(user_id)# データベースからプライマリーキーを検索してユーザーを取得する
    if user_data:
        return User(id=user_data.id, name=user_data.name, email=user_data.email)
    return None

#====================Blueprint設定====================

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(book_register_bp, url_prefix='/book_register')
app.register_blueprint(summary_bp, url_prefix='/summary')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)