# This script can create the database tables based on your models
from peewee import *
from applicant import Applicant
from connection import Connection
from city import City
from closest import Closest
from interview import Interview
from mentor import Mentor
from school import School
from example_data import ExampleData


class Build(Connection):
    """makes the tables and fills them up with example data using ExampleData class"""
    # create tables then fills them up with data
    @classmethod
    def create_tables(cls):

        cls.db.connect()

        cls.delete()
        try:
            cls.db.create_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
            print('Tables were created.')
        except OperationalError:
            print('Tables already exists.')

    # deletes tables
    @classmethod
    def delete(cls):
        cls.db.drop_tables([City, School, Applicant, Closest, Mentor, Interview], safe=True)
        print("Tables deleted.")

    # fill it up with data
    @staticmethod
    def upload_data():
        ExampleData.create_cities()
        ExampleData.create_school()
        ExampleData.create_closest()
        ExampleData.create_mentor()
        ExampleData.create_interview()
        ExampleData.create_applicants()
        print('Tables updated with example data.')
