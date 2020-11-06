import smtplib, ssl, os


USERNAME = os.environ['USERNAME']

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "developercobanov@gmail.com"
receiver_email = "developercobanov@gmail.com"
password = "Mc.1837837"

message = f"""\
Subject: Hi there

This message is sent from {USERNAME}."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)