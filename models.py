from peewee import *
from connection import db
from datetime import date
from datetime import time
# from build import get_dsn, create, set_db
# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class City(BaseModel):
    cid = PrimaryKeyField()
    name = CharField()


class School(BaseModel):
    sid = PrimaryKeyField()
    name = CharField()
    cid = ForeignKeyField(City, related_name="school_location")


class Mentor(BaseModel):
    mid = PrimaryKeyField()
    name = CharField()
    school_id = ForeignKeyField(School, related_name='mentor_school')

class Interview(BaseModel):
    iid = PrimaryKeyField()
    day = DateField()
    start = TimeField()
    end = TimeField()
    mentor_id = ForeignKeyField(Mentor, related_name='mentor_interview')
    reserved = BooleanField(default=False)

class Applicant(BaseModel):
    aid = PrimaryKeyField()
    name = CharField()
    application_code = IntegerField(null=True)
    home_cid = ForeignKeyField(City, related_name="home_location")
    school_cid = ForeignKeyField(City, related_name="school_loc", null=True)
    interview = ForeignKeyField(Interview, related_name='applicant_interview', null=True, default=None)


class Closest(BaseModel):
    clid = PrimaryKeyField()
    home_cid = ForeignKeyField(City, related_name="from_location")
    school_cid = ForeignKeyField(City, related_name="to_location")
