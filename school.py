from peewee import *
from models import BaseModel
from city import City


class School(BaseModel):
    """stores schools model/table"""
    sid = PrimaryKeyField()
    name = CharField()
    cid = ForeignKeyField(City, related_name="school_location")
