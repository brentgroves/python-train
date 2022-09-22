# https://realpython.com/python-send-email/
# https://stackoverflow.com/questions/54717112/how-to-speed-up-sending-file-using-smtp
import smtplib, ssl
from smtplib import SMTPException
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "brent.groves@gmail.com"  # Enter your address
receiver_email = "bgroves@buschegroup.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
password = 'Messiah1!$'
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
  try:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
  except SMTPException:
    print("Error: unable to send email")       
