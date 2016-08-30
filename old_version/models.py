from peewee import *
from connection import Connection


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = Connection.set_db()
