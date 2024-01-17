from email.mime.text import MIMEText
import smtplib

# メール送信処理
def send_mail(send_message, to_email, from_email, account, password, smtp_server, smtp_port):
    """
    メール送信処理
    :param send_message: 送信メッセージ
    :param to_email: 送信先メールアドレス
    :param from_email: 送信元メールアドレス
    :param account: メールのアカウント　メールアドレスと同じ場合が多い
    :param password: メールのパスワード
    :param smtp_server: メールサーバー　
    :param smtp_port: メールサーバーのポート番号
    :return:
    """
    # メール情報設定
    subject = "物体検出で閾値を下回りました"
    msg = MIMEText(send_message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    # SMTPサーバーへ接続
    # server = smtplib.SMTP(smtp_server, smtp_port, timeout=5)

    # SMTPサーバーへ接続(SSL)
    server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=5)
    # ログイン認証
    server.login(account, password)

    # メール送信
    server.send_message(msg)
    # SMTPサーバー切断
    server.quit()
