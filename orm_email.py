from applicant import Applicant
from mentor import Mentor
from connection import Connection
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OrmEmail(Connection):
    """creates messages and sends e-mails"""

    # msg sends e-mail to applicant
    @classmethod
    def send(cls):
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
        msg_list = []
        if len(data_list) >= 1:
            for data in data_list:
                msg = MIMEText('Hi ' + data['name'] + ","
                               + "\n\nI am happy to inform you that we received your application to Codecool."
                               + "\nThe closest Codecool School to you is in " + data['city'] + "."
                               + "\nYour application code is " + str(data['ap_code']) + "."
                               + "\n\nRegards,\nCodecool Team")
                msg['Subject'] = 'Congratulation'
                msg['From'] = 'dog5.laboratories@gmail.com'
                msg['To'] = data['email']
                msg_list.append(msg)
            return msg_list
        else:
            print("All email have been sent.")
            return msg_list
