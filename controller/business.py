from model.applicant import Applicant
from model.email_orm import OrmEmail
from setup.setup_email import ConnectEmail
from model.email_log_decorator import LogDecorator
from model.email_log import LogEmail


# This function manages the submit function from the /registration route
def register_applicant(reg_dict):
    reg_dict_processed = reg_dict
    applicant = Applicant.build_new(reg_dict)
    if applicant.registration_error_set == set():
        email = OrmEmail(**applicant.new_app_email)
        server = ConnectEmail.build_from_file()
        LogDecorator(email).send(server)
        applicant.new_app_sent()
        return None
    else:
        reg_dict_processed['error'] = applicant.registration_error_set
        return(reg_dict_processed)

def login(password):
    return Applicant.get_login(password)

def show_table():
    return LogEmail.all_email()