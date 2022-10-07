from email.message import EmailMessage
from email_sender import email_password

import ssl
import smtplib

email_sender = 'jessecalvin5@gmail.com'
# For email_password; I created a variable in another file and imported the file (email_password) because of security reasons
email_password = email_password

email_receiver = 'christiansilvester700@gmail.com'

subject = 'Email sender using python'
body = '''
Hi, I just wanna say you look Great!
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


