# This script can create the database tables based on your models
from peewee import *
from model.applicant import Applicant
from model.city import City
from model.closest import Closest
from model.interview import Interview
from model.mentor import Mentor
from model.school import School
from model.interview_slot import InterviewSlot
from model.email_log import LogEmail
from setup.example_data import ExampleData


class Build():
    """makes the tables and fills them up with example data using ExampleData class"""

    @classmethod
    def create_tables(cls, db):
        db.connect()
        cls.delete(db)
        try:
            db.create_tables([City, School, Applicant, Closest, Mentor, Interview, InterviewSlot, LogEmail], safe=True)
            return print("Tables were created")
        except OperationalError:
            return print("Tables already exists.")

    @staticmethod
    def delete(db):
        db.drop_tables([City, School, Applicant, Closest, Mentor, Interview, InterviewSlot, LogEmail], safe=True, cascade = True)
        return print("Tables deleted.")

    @staticmethod
    def upload_data():
        ExampleData.create_cities()
        ExampleData.create_school()
        ExampleData.create_closest()
        ExampleData.create_mentor()
        ExampleData.create_interview()
        ExampleData.create_applicants()
        ExampleData.create_scheduled_interviews()
        return print("Tables updated with example data.")
