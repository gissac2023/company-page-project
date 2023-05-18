import smtplib, ssl, os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.environ.get("username")
    print(username)
    password = os.environ.get("password")
    print(password)
    context = ssl.create_default_context()
    receiver = os.environ.get("username")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
