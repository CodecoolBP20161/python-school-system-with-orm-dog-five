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

    @classmethod
    def log(cls, type, to, body, subject):
        log = cls(type=type, to=to, body=body, subject=subject)
        log.save()

    @classmethod
    def all_email(cls):
        return cls.select()



