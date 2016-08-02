from peewee import *
from models import *

class Mentor(BaseModel):
    mid = PrimaryKeyField()
    name = CharField()
    school_id = ForeignKeyField(School, related_name='mentor_school')
