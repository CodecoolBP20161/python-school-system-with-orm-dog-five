from model.applicant import Applicant
from model.email_orm import OrmEmail


# This function manages the submit function from the /registration route
def register_applicant(reg_dict):
    reg_dict_processed = reg_dict
    applicant = Applicant.build_new(reg_dict)
    if applicant.registration_error_set == set():
        email = OrmEmail(applicant.new_app_email)
        email.send()
        applicant.new_app_sent()
        return None
    else:
        reg_dict_processed['error'] = applicant.registration_error_set
        return(reg_dict_processed)