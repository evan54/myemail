from protonmail.client import Client

USERNAME = 'efarmogi'
PASSWORD = r';S/}mgHV;Y]Tu:XcL\HbW7!{*bJBJ!y#e6z%n$vgJ'

EVAN_ADDRESS = 'evan54@gmail.com'
ANGIE_ADDRESS = 'angie.scouros@gmail.com'
MY_ADDRESSES = [EVAN_ADDRESS, ANGIE_ADDRESS]


def send_email(to, subject='', body='', cc='', bcc=''):
    client = Client()
    client.blocking = True
    client.Username = USERNAME
    client.api.login(PASSWORD)

    client._send_simple(to, subject, body, cc, bcc)


def send_us_an_email(subject, body):
    send_email(MY_ADDRESSES, subject, body)


def send_me_an_email(subject, body):
    send_email(EVAN_ADDRESS, subject, body)
