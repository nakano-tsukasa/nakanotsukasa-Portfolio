#====================パッケージインストール====================
from flask_sqlalchemy import SQLAlchemy#SQLAlchemyのORM(Object-Relational Mapping)機能を使って、Pythonのクラスとデータベースを関連付ける
import pymysql
pymysql.install_as_MySQLdb()

#====================DB====================
db = SQLAlchemy()#SQLAlchemyクラスのインスタンス化

#db.Modelを継承して、データベースのテーブルに対応するクラスを定義する。.ModelはSQLAlchemyが用意する基底クラス。
#このクラスを継承することで、モデルクラスがデータベーステーブルとマッピングされ、ORM機能が利用できるようになる。
class User_profiles(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)#このクラスの属性がデータベースのカラムに対応する。
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)