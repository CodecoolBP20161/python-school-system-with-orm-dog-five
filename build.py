# This script can create the database tables based on your models
from peewee import *
from applicant import Applicant
from connection import Connection
from city import City
from closest import Closest
from interview import Interview
from mentor import Mentor
from school import School


class Build(Connection):
    @classmethod
    def create(cls):
        cls.db.connect()

        cls.delete()
        try:
            cls.db.create_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
            print('Tables were created')
        except OperationalError:
            print('Tables already exists')

    @classmethod
    def delete(cls):
        cls.db.drop_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
        print("Deleted...")
