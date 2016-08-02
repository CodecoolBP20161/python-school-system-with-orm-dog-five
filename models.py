from peewee import *
from connection import db
from datetime import date
from datetime import time
# from build import get_dsn, create, set_db
# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
