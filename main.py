from setup.setup import setup_db_all
from setup.setup import setup_email_all
from setup.setup import start_web_server


user_input = input("Hello! Would you like to:\
                   \n1. Set up your database (WARNING: this will delete all your data!)\
                   \n2. Start web server\
                   \n3. Set up e-mail stuff\
                   \n4. Update new applicants with code and closest school\
                   \n5. Schedule interviews\
                   \n6. Send e-mails to new applicants\
                   \n")

if user_input == "1":
    setup_db_all()

elif user_input == "2":
    start_web_server()

elif user_input == "3":
    setup_email_all()

elif user_input == "4":
    pass

elif user_input == "5":
    pass

else:
    print("Bye")
