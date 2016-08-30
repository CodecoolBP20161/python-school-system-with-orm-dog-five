from peewee import *
from model.basemodel import BaseModel
import datetime


class LogEmail(BaseModel):
    """Email logging"""
    type = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    email = CharField()
    subject = CharField()
    body = CharField()
