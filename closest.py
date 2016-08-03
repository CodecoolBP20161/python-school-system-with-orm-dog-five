from peewee import *
from models import *
from city import City


class Closest(BaseModel):
    clid = PrimaryKeyField()
    home_cid = ForeignKeyField(City, related_name="from_location")
    school_cid = ForeignKeyField(City, related_name="to_location")
