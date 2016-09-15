from model.email_log import LogEmail

class LogDecorator:
    def __init__(self, send_message):
        log_dict = {'type': send_message.type,
                    'to': send_message.to,
                    'body': " ".join(send_message.body.splitlines())[:140],
                    'subject': send_message.subject}
        LogEmail.log(**log_dict)
        self.send_message = send_message

    def send(self, server):
        self.send_message.send(server)