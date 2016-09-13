# This script can create the database tables based on your models
from peewee import *
from setup.setup_database import ConnectDB
from setup.example_data import ExampleData
from model.applicant import Applicant
from model.city import City
from model.closest import Closest
from model.interview import Interview
from model.mentor import Mentor
from model.school import School
from model.interview_slot import InterviewSlot
from model.email_log import LogEmail
from setup.example_data import ExampleData


class Build(ConnectDB):
    """makes the tables and fills them up with example data using ExampleData class"""
    # create tables then fills them up with data
    @classmethod
    def create_tables(cls):
        cls.db.connect()
        cls.delete()
        try:
            cls.db.create_tables([City, School, Applicant, Closest, Mentor, Interview, InterviewSlot, LogEmail], safe=True)
            return_message = "Tables were created"
            print(return_message)
            return(return_message)
        except OperationalError:
            return_message = "Tables already exists."
            print(return_message)
            return(return_message)

    # deletes tables
    @classmethod
    def delete(cls):
        cls.db.drop_tables([City, School, Applicant, Closest, Mentor, Interview, InterviewSlot, LogEmail], safe=True, cascade = True)
        return_message = "Tables deleted."
        print(return_message)
        return(return_message)

    # fill it up with data
    @staticmethod
    def upload_data():
        ExampleData.create_cities()
        ExampleData.create_school()
        ExampleData.create_closest()
        ExampleData.create_mentor()
        ExampleData.create_interview()
        ExampleData.create_applicants()
        ExampleData.create_scheduled_interviews()
        return_message = "Tables updated with example data."
        return(return_message)
