from applicant import Applicant
from mentor import Mentor
from connection import Connection
from smtplib import *


class email(Connection):
    """creates messages and send e-mails"""

    # Connection has class attribute server, etc
    # msg and login comes from applicant and here
    @classmethod
    def send(cls, msg, login):
        # receive msg object, login info and send email via smtplib method
        pass

    @staticmethod
    def create_newapp():
        # use applicant method to get info then make msg object
        pass
