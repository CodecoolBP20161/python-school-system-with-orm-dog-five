from setup.setup import setup_db_all
from setup.setup import setup_email_all
from setup.setup import start_web_server
from setup.setup import process_new_applicant
from setup.setup import process_acceptance


user_input = '0'
while user_input != 'q':
    user_input = input('Hello! Would you like to:\
                       \n1. Set up your database (WARNING: this will delete all your data!)\
                       \n2. Start web server\
                       \n3. Set up e-mail stuff\
                       \n4. Update new applicants with code and closest school\
                       \n5. Schedule interviews\
                       \n6. Send e-mails to new applicants\
                       \nq quit\
                       \n')
    if user_input == '1':
        setup_db_all()
    if user_input == '2':
        start_web_server()

    if user_input == '3':
        setup_email_all()

    if user_input == '4':
        process_new_applicant()

    if user_input == '5':
        process_acceptance()

    if user_input == '5':
        process_acceptance()