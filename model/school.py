from peewee import *
from model.basemodel import BaseModel
from model.city import City


class School(BaseModel):
    """city table/model"""
    name = CharField()
    city = ForeignKeyField(City, related_name="school_location")

