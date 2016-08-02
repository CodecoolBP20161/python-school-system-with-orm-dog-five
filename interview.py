from peewee import *
from models import *
from mentor import Mentor


class Interview(BaseModel):
    iid = PrimaryKeyField()
    day = DateField()
    start = TimeField()
    end = TimeField()
    mentor_id = ForeignKeyField(Mentor, related_name='mentor_interview')
    reserved = BooleanField(default=False)
