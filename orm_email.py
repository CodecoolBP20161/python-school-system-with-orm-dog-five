from applicant import Applicant
from mentor import Mentor
from connection import Connection
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OrmEmail(Connection):
    """creates messages and send e-mails"""

    # Connection has class attribute server, etc
    # msg and login comes from applicant and here
    @classmethod
    def send(cls):
        # receive msg object, login info and send email via smtplib method
        msg = cls.create_newapp()
        server, fromaddr, password = Connection.set_smtp()
        server.starttls()
        server.login(fromaddr, password)
        server.send_message(msg)
        server.quit()


    @classmethod
    def create_newapp(cls):
        smtp_stuff = cls.create_newapp()
        msg = MIMEText('helloooo')
        msg['Subject'] = 'targy'
        msg['From'] = 'dog5.laboratories@gmail.com'
        msg['To'] = 'dog5.laboratories@gmail.com'
        return msg

OrmEmail.send()
