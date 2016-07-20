# This script can create the database tables based on your models
from peewee import *
from models import *
from connection import db

def create(db):
    db.connect()
    #db.drop_table([City, School, Applicant, Closest])
    try:
        db.create_tables([City, School, Applicant, Closest], safe=True)
        print('Tables were created')
    except OperationalError:
        print('Tables already exists')

create(db)
