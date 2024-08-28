#====================パッケージインストール====================

import jwt#JSON Web Token インストールはPyJWT
import datetime
import os#.envファイルからos.getenvで環境変数を取得する。osはファイルパスの操作もできる。

SECRET_KEY = os.getenv('SECRET_KEY')#この秘密鍵はJWTの署名に使われる。

#--------------------入力されたメールアドレスからトークンをエンコードする--------------------

def generate_verification_token(email):
    payload = {#JSONのペイロード（データ部分）を定義する。ユーザーのメールアドレスを含むJWTを生成する。
        'email': email,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)#今の時間に有効期限1時間を足したものが期限となる。
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')#ペイロードを指定した秘密鍵でHS256アルゴリズムを用いて署名し、JWTを生成する。

#--------------------認証リンクに含まれるトークンをデコードする--------------------

def verify_verification_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])#jwt.decodeメソッドを用いて、トークンをでコードし、ペイロード取得する。指定された秘密鍵でHS256アルゴリズムを用いて検証する。
        return payload['email']#payloadのemailキーの値を返す。
    except jwt.ExpiredSignatureError:#期限切れにより発生する例外をキャッチする。
        raise ValueError("Token has expired.")#トークンが期限切れである場合に、エラーメッセージを表示する。
    except jwt.InvalidTokenError:#無効なトークンである場合に発生する例外をキャッチする。
        raise ValueError("Invalid token.")