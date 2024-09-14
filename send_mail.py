import smtplib, ssl
import os


def send_email(content):
    host = "smtp.gmail.com"
    port = 465

    username = "infocukamuran@gmail.com"
    password = os.getenv("PASS3")
    reciever = "infocukamuran@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, content)