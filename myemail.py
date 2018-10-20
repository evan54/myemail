import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import O365, TO_ADDRESSES


def send_email(to, subject='', body='', cc='', bcc=''):

    if isinstance(to, (tuple, list)):
        to = ', '.join(to)

    server = smtplib.SMTP(O365.SERVER, 587)
    server.starttls()
    server.login(O365.USERNAME, O365.PASSWORD)
    msg = MIMEMultipart()

    msg['From'] = O365.USERNAME
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    return server.send_message(msg)


def send_us_an_email(subject, body):
    send_email(TO_ADDRESSES.BOTH, subject, body)


def send_me_an_email(subject, body):
    send_email(TO_ADDRESSES.EVAN, subject, body)
