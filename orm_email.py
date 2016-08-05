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
    def send(cls,msg_list):
        server, fromaddr, password = Connection.set_smtp()
        server.starttls()
        server.login(fromaddr, password)
        print("Sending e-mails, please wait.")
        for msg in msg_list:
            server.send_message(msg)
        server.quit()
        print("DONE.")

    # create the message object for the send
    # to avoid empty e-mails, use after new applicants have been updated
    @classmethod
    def create_newappl_msg(cls):
        try:
            data_list = Applicant.to_newappl_msg()
            msg_list = []
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
        except StopIteration:
            print("Can't create messages. Assign school and generate code fist.")
            quit()

    @classmethod
    def create_mentor_interview_msg(cls):
        try:
            data_list = Mentor.to_mentor_interview_msg()
            msg_list = []
            for data in data_list:
                msg = MIMEText('Hi ' + data['m_name'] + ","
                               + "\n\nThere was an interview scheduled for you."
                               + "\nApplicant's name is " + data['ap_name'] + "."
                               + "\nIt will be in " + data['city'] + ". At " + str(data['date'])\
                               + " from " + str(data['start_time']) + " to " + str(data['start_time']) + "."
                               + "\n\nRegards,\nCodecool Team")
                msg['Subject'] = 'Congratulation'
                msg['From'] = 'dog5.laboratories@gmail.com'
                msg['To'] = data['email']
                msg_list.append(msg)
            return msg_list
        except StopIteration:
            print("Can't create messages. Assign school and generate code fist.")
            quit()
