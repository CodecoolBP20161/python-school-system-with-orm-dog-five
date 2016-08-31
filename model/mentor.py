from peewee import *
from model.basemodel import BaseModel
from model.school import School


class Mentor(BaseModel):
    """Mentor info"""
    name = CharField()
    school = ForeignKeyField(School, related_name='mentor_school')
