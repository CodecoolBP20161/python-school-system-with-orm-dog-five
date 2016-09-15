from email.mime.text import MIMEText

class OrmEmail():
    """creates messages and sends e-mails"""

    def __init__(self, body, subject, to, type):
        self.body = body
        self.subject = subject
        self.to = to
        self.type = type
        self.MIMEText_obj = MIMEText(body)
        self.MIMEText_obj['Subject'] = subject
        self.MIMEText_obj['To'] = to

    # server info is inherited from the ConnectEmail class
    def send(self, server):
        self.MIMEText_obj['From'] = server.fromaddr
        server.server.starttls()
        server.server.login(server.fromaddr, server.password)
        server.server.send_message(self.MIMEText_obj)
        server.server.quit()
