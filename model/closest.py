from peewee import *
from model.basemodel import BaseModel
from model.city import City
from model.school import School


class Closest(BaseModel):
    """stores the pairing of closest cities"""
    home = ForeignKeyField(City, related_name="from_location")
    school = ForeignKeyField(School, related_name="to_location")
