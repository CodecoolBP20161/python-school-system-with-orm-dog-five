from models import *
from build import Build
from connection import Connection
from example_data import *
from applicant import Applicant
# Write here your console application

user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Update new applicants\
                   \n")

if user_input == "1":
    Build.create()
    create_cities()
    create_school()
    create_closest()
    create_mentor()
    create_interview()
    create_applicants()

elif user_input == "2":
    Applicant.get_closest_school()
    Applicant.update_appl_code()

else:
    print("Bye")
