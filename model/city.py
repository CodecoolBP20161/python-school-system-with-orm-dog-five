from peewee import *
from model.basemodel import BaseModel


class City(BaseModel):
    """city table/model"""
    name = CharField()
