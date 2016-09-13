from setup.setup_email import ConnectEmail
from email.mime.text import MIMEText

class OrmEmail():
    """creates messages and sends e-mails"""

    def __init__(self, msg_data):
        self.body = msg_data['Body']
        self.subject = msg_data['Subject']
        self.toaddr = msg_data['To']
        self.type = msg_data['Type']

        msg = MIMEText(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr

        self.MIMEText_obj = msg


    # server info is inherited from the ConnectEmail class
    def send(self):
        ConnectEmail.server.starttls()
        ConnectEmail.server.login(ConnectEmail.fromaddr, ConnectEmail.password)
        ConnectEmail.server.send_message(self.MIMEText_obj)
        ConnectEmail.server.quit()

