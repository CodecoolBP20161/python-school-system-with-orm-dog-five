from applicant import Applicant
from mentor import Mentor
from connection import Connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OrmEmail(Connection):
    """creates messages and sends e-mails"""

    # Connection has class attribute server, etc
    # msg and login comes from applicant and here
    @classmethod
    def send(cls):
        # receive msg object, login info and send email via smtplib method
        msg_list = cls.create_newappl_msg()
        server, fromaddr, password = Connection.set_smtp()
        server.starttls()
        server.login(fromaddr, password)
        for msg in msg_list:
            server.send_message(msg)
        server.quit()

    # create the message object for the send
    # to avoid empty e-mails, use after new applicants have been updated
    @classmethod
    def create_newappl_msg(cls):
        data_list = Applicant.to_send_email()
        msg_list = data_list
        for data in data_list:
            msg = MIMEText('Hi ' + data[1] + "!")
            msg['Subject'] = 'Congratulation'
            msg['From'] = 'dog5.laboratories@gmail.com'
            msg['To'] = record.email
            msg_list.append(msg)
        return msg_list
