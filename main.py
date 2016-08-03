# RUN THIS TO START PROGRAM

from models import *
from build import Build
from connection import Connection
from applicant import Applicant
from orm_email import OrmEmail
from interview import Interview


# Get user input to reach functions
user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Set up e-mail stuff\
                   \n3. Update new applicants with code, reserve interview and send e-mail\
                   \n")

if user_input == "1":
    Build.create_tables()
    Build.upload_data()

if user_input == "2":
    Connection.set_smtp()

elif user_input == "3":
    Applicant.get_closest_school()
    Applicant.update_appl_code()

    Interview.reserved_interview_to_applicant()

    a = OrmEmail.create_newappl_msg()
    for x in a:
        print(x)

#    OrmEmail.send()

else:
    print("Bye")
