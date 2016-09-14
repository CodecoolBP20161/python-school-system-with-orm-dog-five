from peewee import *
from model.basemodel import BaseModel
import datetime


class LogEmail(BaseModel):
    """Email logging"""
    type = TextField()
    to = TextField()
    subject = TextField()
    body = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    def __init__(self, send_message):
        log_dict = {'type': send_message.type,
                  'to': send_message.to,
                  'body': " ".join(send_message.body.splitlines())[:140],
                  'subject': send_message.subject}
        super().__init__(**log_dict)
        self.send_message = send_message

    def send(self, server):
        self.send_message.send(server)
        self.save()

    @classmethod
    def all_email(cls):
        return cls.select()



