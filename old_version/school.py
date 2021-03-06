from peewee import *
from model.basemodel import BaseModel
from model.city import City


class School(BaseModel):
    """stores schools model/table"""
    sid = PrimaryKeyField()
    name = CharField()
    cid = ForeignKeyField(City, related_name="school_location")
