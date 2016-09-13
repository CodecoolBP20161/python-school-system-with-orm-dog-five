from model.applicant import Applicant


# This function manages the submit function from the /registration route
def register_applicant(reg_dict):
    reg_dict_processed = reg_dict
    applicant = Applicant.build_new(reg_dict)
    if applicant.registration_error_set == set():
        # email(applicant)
        return None
    else:
        reg_dict_processed['error'] = applicant.registration_error_set
        return(reg_dict_processed)