# RUN THIS TO START PROGRAM

from models import *
from build import Build
from connection import Connection
from applicant import Applicant


# Get user input to reach functions
user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Update new applicants\
                   \n")

if user_input == "1":
    Build.create_tables()
    Build.upload_data()

elif user_input == "2":
    Applicant.get_closest_school()
    Applicant.update_appl_code()

    Interview.reserved_interview_to_applicant()

else:
    print("Bye")
