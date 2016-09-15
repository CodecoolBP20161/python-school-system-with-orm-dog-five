# this needs work, how to import from another folder?
from peewee import *
from setup.setup_database import ConnectDB


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = ConnectDB.build_from_file().db
