#!/miniconda/bin/python
#!/usr/bin/python
# https://realpython.com/python-send-email/
# https://docs.python.org/3/library/smtplib.html
# https://www.tutorialspoint.com/python/python_sending_email.htm
# https://www.ionos.com/digitalguide/e-mail/technical-matters/smtp/
import smtplib
from smtplib import SMTPException
from smtplib import SMTP

sender = 'mcp@mobexglobal.com'
receivers = ['bgroves@buschegroup.com']

message = """From: Mobex Computing Platform <mcp@mobexglobal.com>
To: Brent Groves <bgroves@buschegroup.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

# try:
#    smtpObj = smtplib.SMTP('mobexglobal-com.mail.protection.outlook.com')
#    smtpObj.sendmail(sender, receivers, message)         
#    print("Successfully sent email")
# except Exception:
#    print("Error: unable to send email")
# with SMTP('mobexglobal-com.mail.protection.outlook.com') as smtp:
   # smtp.noop()
try:
   with SMTP('mobexglobal-com.mail.protection.outlook.com') as smtp:
      print(smtp.noop())
      print(smtp.ehlo_or_helo_if_needed())
      print(smtp.docmd('SIZE', args=''))
      # print(smtp.verify('gphillips'))
      # print(smtp.verify('gphillips@buschegroup.com'))
      print(smtp.verify('gphillips@mobexglobal.com'))
      smtp.quit()
   # smtp = smtplib.SMTP('mobexglobal-com.mail.protection.outlook.com')
   # smtp.noop()
   # ret = smtp.verify('gphillips')
   # smtp.quit()
   # smtpObj.sendmail(sender, receivers, message)         
   # print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")   