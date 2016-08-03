from peewee import *
from models import BaseModel
from school import School


class Mentor(BaseModel):
    """peeweee BaseModel"""
    mid = PrimaryKeyField()
    name = CharField()
    school_id = ForeignKeyField(School, related_name='mentor_school')
