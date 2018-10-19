import smtplib
from O365 import Message

USERNAME = 'efarmogimoy@hotmail.com'
PASSWORD = r';S/}mgHV;Y]Tu:XcL\HbW7!{*bJBJ!y#e6z%n$vgJ'

# SERVER = 'smtp-mail.outlook.com'
SERVER = 'smtp.office365.com'
FOM = USERNAME

EVAN_ADDRESS = 'evan54@gmail.com'
ANGIE_ADDRESS = 'angie.scouros@gmail.com'
MY_ADDRESSES = [EVAN_ADDRESS, ANGIE_ADDRESS]


def send_email(to, subject='', body='', cc='', bcc=''):
    server = smtplib.SMTP(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, to, subject)


def send_us_an_email(subject, body):
    send_email(MY_ADDRESSES, subject, body)


def send_me_an_email(subject, body):
    send_email(EVAN_ADDRESS, subject, body)


def send():
    fromaddr = USERNAME
    toaddrs = ['evan54@gmail.com']
    msg = '''
        From: {fromaddr}
        To: {toaddr}
        Subject: testin'

        This is a test
        .
    '''

    msg = msg.format(fromaddr=fromaddr, toaddr=toaddrs[0])
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', port=25)
    server.starttls()
    server.ehlo("example.com")
    server.mail(fromaddr)
    server.rcpt(toaddrs[0])
    server.data(msg)
    server.quit()


def send_o365():

    authenticiation = (USERNAME, PASSWORD)
    m = Message(auth=authenticiation)
    m.setRecipients('reciving@office365.com')
    m.setSubject('I made an email script.')
    m.setBody('Talk to the computer, cause the human does not want to hear')
    m.sendMessage()
