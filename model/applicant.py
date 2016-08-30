from peewee import *
from model.basemodel import BaseModel
from model.city import City
from model.school import School

class Applicant(BaseModel):
    """Applicant model/table and data manipulation related to it"""
    name = CharField()
    application_code = IntegerField(null=True, unique=True)
    home = ForeignKeyField(City, related_name="appl_home")
    school = ForeignKeyField(School, related_name="appl_school", null=True)
    # in real life this should be unique, but we send all e-mails to the same e-mail account in our test data
    email = CharField()
    sent_application_email = BooleanField(default=False)
    sent_interview_email = BooleanField(default=False)
    code_set = set()
