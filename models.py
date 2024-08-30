#====================パッケージインストール====================
from flask_sqlalchemy import SQLAlchemy#SQLAlchemyのORM(Object-Relational Mapping)機能を使って、Pythonのクラスとデータベースを関連付ける
import pymysql
pymysql.install_as_MySQLdb()

from flask_login import UserMixin

#====================データベースの設定====================

db = SQLAlchemy()#SQLAlchemyクラスのインスタンス化

#db.Modelを継承して、データベースのテーブルに対応するクラスを定義する。.ModelはSQLAlchemyが用意する基底クラス。
#このクラスを継承することで、モデルクラスがデータベーステーブルとマッピングされ、ORM機能が利用できるようになる。
class User_profiles(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)#このクラスの属性がデータベースのカラムに対応する。
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    books = db.relationship('Books', back_populates='owner', lazy=True)
    summaries = db.relationship('Summaries', back_populates='author', lazy=True)

class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'), nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=True)
    published_date = db.Column(db.Date, nullable=True)
    owner = db.relationship('User_profiles', back_populates='books', lazy=True)
    book_summaries = db.relationship('Summaries', back_populates='book_summary', lazy=True)

class Summaries(db.Model):
    __tablename__='summaries'
    summary_id = db.Column(db.Integer,  primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    summary_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    author = db.relationship('User_profiles', back_populates='summaries',  lazy=True)
    book_summary = db.relationship('Books', back_populates='book_summaries', lazy=True)

#====================Flask-Loginの設定====================

class User(UserMixin):# UserMixinクラスの継承。is_authenticated, is_active, is_anonymous, get_id()などのメソッドやプロパティを持つ
    def __init__(self, id, name, email):# Userクラスのコンストラクタ__init__メソッド
        self.id = id# Flask-LoginはこのIDを使ってユーザーを識別する。
        self.name = name
        self.email = email