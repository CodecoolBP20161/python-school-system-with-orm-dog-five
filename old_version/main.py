# RUN THIS TO START PROGRAM

from models import *
from build import Build
from connection import Connection
from applicant import Applicant
from orm_email import OrmEmail
from interview import Interview
from interview_slot import InterviewSlot


# Get user input to reach functions
user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Set up e-mail stuff\
                   \n3. Update new applicants with code and closest school\
                   \n4. Schedule interviews\
                   \n5. Send e-mails to new applicants\
                   \n")

if user_input == "1":
    Build.create_tables()
    Build.upload_data()

elif user_input == "2":
    Connection.set_smtp()

elif user_input == "3":
    Applicant.get_closest_school()
    Applicant.update_appl_code()

elif user_input == "4":
    InterviewSlot.schedule()

elif user_input == "5":
    msg_list = OrmEmail.create_newappl_msg()
    OrmEmail.send(msg_list)

else:
    print("Bye")
