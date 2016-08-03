from peewee import *
from models import *


class City(BaseModel):
    cid = PrimaryKeyField()
    name = CharField()
