# Mail Client Tutorial from https://www.youtube.com/watch?v=FGdiSJakIS4

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('mail.server',25)

server.ehlo()

with open('password.txt','r') as f:
    password = f.read()

server.login('username', password)


msg = MIMEMultipart
msg['From'] = 'Jerry'
msg['To'] = 'jim@jimbo.com'
msg['Subject'] = 'Test Mail'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'sample.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('jerry@jerry.com','jim@jimbo.com',text)