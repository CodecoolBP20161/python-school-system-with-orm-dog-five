from peewee import *
from models import *
from city import City


class School(BaseModel):
    sid = PrimaryKeyField()
    name = CharField()
    cid = ForeignKeyField(City, related_name="school_location")
