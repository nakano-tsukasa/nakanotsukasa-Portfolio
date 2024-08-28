#====================パッケージインストール====================

import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

#--------------------f1:認証メール送信--------------------

#Gmailで認証メールを送信する
def send_verification_email(user_email, verification_link):
    load_dotenv()#.envファイルを読み込む、以下4行：環境変数を取得
    smtp_server = os.getenv("SMTP_SERVER")#GmailのSMTPサーバ
    smtp_port = os.getenv("SMTP_PORT")#SSL用ポート、TLSは587
    sender_email = os.getenv("EMAIL_USER")#.envファイルの環境変数から取得する
    sender_password = os.getenv("EMAIL_PASSWORD")#セキュリティ強化のためにapp passwordを使用する

    subject = "Sign-up confirmation email"#以下６行：メール内容、詳細設定
    body = f"Please click on this link to verify your identity.\nVerification Link: {verification_link}"
    message = MIMEText(body)#オプション引数でhtmlの形にしたり、文字種を変えることができる
    message['Subject'] = subject#MIMEText()はemail.mime.textモジュールにあるクラスであり、Messageクラスというヘッダーを辞書型のように操作するための機能を有するクラスを継承している。
    message['From'] = sender_email
    message['To'] = user_email

    try:#エラーが発生する可能性があるコードを囲むために使う
        with smtplib.SMTP_SSL(smtp_server,smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, message.as_string())#as_string()はemail.message.EmailMessageオブジェクトやemail.mime.text.MIMETextオブジェクトを文字列として取得する
        print("Confirmation email sent.")
    except Exception as e:
        print(f"Mail Sending Error: {e}")
