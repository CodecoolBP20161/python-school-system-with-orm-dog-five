from setup.setup_email import ConnectEmail
from email.mime.text import MIMEText

class OrmEmail():
    """creates messages and sends e-mails"""

    def __init__(self, msg_data):
        self.server, self.fromaddr, self.password = ConnectEmail.set_smtp()
        self.body = msg_data['Body']
        self.subject = msg_data['Subject']
        self.toaddr = msg_data['To']
        self.type = msg_data['Type']

        msg = MIMEText(self.body)
        msg['Subject'] = self.subject
        msg['From'] = ConnectEmail.fromaddr
        msg['To'] = self.toaddr

        self.MIMEText_obj = msg


    # server info is inherited from the ConnectEmail class
    def send(self):
        self.server.starttls()
        self.server.login(self.fromaddr, self.password)
        self.server.send_message(self.MIMEText_obj)
        self.server.quit()

