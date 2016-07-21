from peewee import *
from connection import db
# from build import get_dsn, create, set_db
# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class City(BaseModel):
    CID = PrimaryKeyField()
    name = CharField()


class School(BaseModel):
    SID = PrimaryKeyField()
    name = CharField()
    CID = ForeignKeyField(City, related_name="school_location")


class Applicant(BaseModel):
    AID = PrimaryKeyField()
    name = CharField()
    application_code = IntegerField()
    home = ForeignKeyField(City, related_name="home_location")


class Closest(BaseModel):
    CLID = PrimaryKeyField()
    Home_CID = ForeignKeyField(City, related_name="from_location")
    School_CID = ForeignKeyField(City, related_name="to_location")
