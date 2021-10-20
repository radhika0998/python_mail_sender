import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465 # For SSL, and 587 for starttls

username = 'name@gmail.com' #username or Email Address of Sender'
password = '16-digit passcode'
sender_email = 'name@gmail.com'
recipients = ['recipient1@example.com', 'recipient2@example.com']

msg = MIMEText("""Hi there,\
\nThis is a test mail.""")
msg['Subject'] = 'Test Mail'
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender_email, recipients, msg.as_string())
server.quit()
