from peewee import *
from models import BaseModel


class City(BaseModel):
    """city table/model"""
    cid = PrimaryKeyField()
    name = CharField()
