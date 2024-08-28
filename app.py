#====================パッケージインストール====================

from flask import Flask#Webサーバ構築用パッケージ
from models import db#データベースのモデル（ORM）の定義を取り込み
import os

from routes.autho_routes import auth_bp
from routes.main_route import main_bp
from routes.account_routes import account_bp

#====================Flask設定、db初期化、secret_keyの設定====================

DBSERVER_URI = os.getenv('DBSERVER_URI')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DBSERVER_URI#あとでadminからuser用のPOST専用DBユーザーに変更する
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#オブジェクトのモディファイを無効にする
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)#dbの初期化

#====================Blueprint設定====================

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(account_bp, url_prefix='/account')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)