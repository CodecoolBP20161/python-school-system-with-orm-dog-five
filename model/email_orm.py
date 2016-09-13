from setup.setup_email import ConnectEmail
from email.mime.text import MIMEText

class OrmEmail():
    """creates messages and sends e-mails"""

    def __init__(self, msg_data):
        msg = MIMEText(msg_data['Body'])
        msg['Subject'] = msg_data['Subject']
        msg['To'] = msg_data['To']
        self.MIMEText_obj = msg
        self.type = msg_data['Type']

    # server info is inherited from the ConnectEmail class
    def send(self, server):
        self.MIMEText_obj['From'] = server.fromaddr
        server.server.starttls()
        server.server.login(server.fromaddr, server.password)
        server.server.send_message(self.MIMEText_obj)
        server.server.quit()
