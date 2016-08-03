from peewee import *
from models import BaseModel
from city import City


class Closest(BaseModel):
    """stores the pairing of closest cities"""
    clid = PrimaryKeyField()
    home_cid = ForeignKeyField(City, related_name="from_location")
    school_cid = ForeignKeyField(City, related_name="to_location")
