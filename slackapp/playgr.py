import os
from dotenv import load_dotenv
import smtplib
import ssl
from email.message import EmailMessage

def send_email(email_sender, email_receiver, subject, body):
    load_dotenv()
    email_password = os.getenv('email_password')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return print(em)

send_email('keviinkibe@gmail.com','kchegz234@gmail.com','test4','test4' )
