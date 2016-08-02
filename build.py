# This script can create the database tables based on your models
from peewee import *
from models import *
from applicant import Applicant
from connection import db
from city import City
from closest import Closest
from interview import Interview
from mentor import Mentor
from school import School


def create(db):
    db.connect()

    delete(db)
    try:
        db.create_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
        print('Tables were created')
    except OperationalError:
        print('Tables already exists')


def delete(db):
    db.drop_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
    print("Deleted...")
