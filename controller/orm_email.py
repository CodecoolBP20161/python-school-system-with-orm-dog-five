from setup.setup_email import ConnectEmail
from email.mime.text import MIMEText

class OrmEmail(ConnectEmail):
    """creates messages and sends e-mails"""

    # msg sends e-mail to applicant
    @classmethod
    def send(cls):
        server, fromaddr, password = ConnectEmail.set_smtp()
        server.starttls()
        server.login(fromaddr, password)
        for msg in msg_list:
            server.send_message(msg)
        server.quit()
        return 'email sent'

    # create the message object for the send
    # to avoid empty e-mails, use after new applicants have been updated
    @classmethod
    def create_newappl_msg(cls):
        try:
            data_list = Applicant.to_newappl_msg()
            msg_list = []
            if len(data_list) >= 1:
                for data in data_list:
                    msg = MIMEText('Hi ' + data['name'] + ","
                                   + "\n\nI am happy to inform you that we received your application to Codecool."
                                   + "\nThe closest Codecool School to you is in " + data['city'] + "."
                                   + "\nYour application code is " + str(data['ap_code']) + "."
                                   + "\n\nRegards,\nCodecool Team")
                    msg['Subject'] = 'Congratulations'
                    msg['From'] = 'dog5.laboratories@gmail.com'
                    msg['To'] = data['email']
                    msg_list.append(msg)
                return msg_list
        except StopIteration:
            return "Can't create messages. Assign school and generate code fist."


    # create the message object for the send
    # to avoid empty e-mails, use after new applicants have been updated
    @classmethod
    def create_appl_interview_msg(cls):
        try:
            data_list = Applicant.to_newappl_msg()
            msg_list = []
            if len(data_list) >= 1:
                for data in data_list:
                    msg = MIMEText("Hi " + data['name'] + ","
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
            return "Can't create messages. Assign school and generate code fist."
