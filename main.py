from setup.setup import setup_db_all
from setup.setup import setup_email_all


user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Set up e-mail stuff\
                   \n3. Update new applicants with code and closest school\
                   \n4. Schedule interviews\
                   \n5. Send e-mails to new applicants\
                   \n")

if user_input == "1":
    setup_db_all()

elif user_input == "2":
    setup_email_all()

elif user_input == "3":
    pass

elif user_input == "4":
    pass

elif user_input == "5":
    pass

else:
    print("Bye")
