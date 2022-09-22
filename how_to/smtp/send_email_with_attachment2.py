#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/envs/etl/bin/python
# https://medium.com/@neonforge/how-to-send-emails-with-attachments-with-python-by-using-microsoft-outlook-or-office365-smtp-b20405c9e63a
# https://medium.com/@neonforge/how-to-send-emails-with-attachments-with-python-by-using-microsoft-outlook-or-office365-smtp-b20405c9e63a
# https://realpython.com/python-send-email/
# https://medium.com/mlearning-ai/use-python-to-send-outlook-emails-d673ce9e33e4

# All Base64 encoding does is take groups of 6 bits of data at a time from an arbitrary blob of data, and map them to inoffensive 
# printable characters. The Base64 character set uses characters that are unlikely to be molested by a wide variety of text conduits. 
# Base64 can also break things up into line-sized chunks, to play well with human readable documents.



import smtplib
# multipurpose internete mail extenstion MIME
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def send_email(email_recipient, email_subject, email_message, attachment_location = ''):
   email_sender = 'mcp@buschegroup.com'

   msg = MIMEMultipart()
   msg['From'] = email_sender
   msg['To'] = email_recipient
   msg['Subject'] = email_subject

   msg.attach(MIMEText(email_message, 'plain'))
   if attachment_location != '':
    filename = os.path.basename(attachment_location)
    attachment = open(attachment_location, "rb")
    part = MIMEBase('application', 'octet-stream')
   #  The application/octet-stream MIME type is used for unknown binary files. 
   # It preserves the file contents, but requires the receiver to determine file type
    part.set_payload(attachment.read())
   #  mail uses 7-bit ASCII and non-ASCII files need to be encoded before using it.
   #  base64 uses A-Za-z0-9 and + / characters only in 6 bit chunks
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
   #  In a regular HTTP response, the Content-Disposition response header is a header indicating 
   #  if the content is expected to be displayed inline in the browser, 
   #  that is, as a Web page or as part of a Web page, or as an attachment, that is downloaded and saved locally
    msg.attach(part)

   try:
      server = smtplib.SMTP('mobexglobal-com.mail.protection.outlook.com')

      # server = smtplib.SMTP('smtp.office365.com', 587)
      # server.ehlo()
      # server.starttls()
      # server.login('bgroves@buschegroup.com', 'JesusLives1!')
      text = msg.as_string()
      server.sendmail(email_sender, email_recipient, text)
      print('email sent')
      server.quit()
   except:
      print("SMPT server connection error")
   return True

send_email('bgroves@buschegroup.com',
           'test2',
           'This is another test', 
           '/home/bgroves@BUSCHE-CNC.COM/src/python-train/how_to/smtp/TB_2021_08_to_2022_08_on_09_19.xlsx')   



