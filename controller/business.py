from model.applicant import Applicant


# This function manages the submit function from the /registration route
def validate(reg_dict):
    Applicant.add_applicant(reg_dict)
    reg_dict_with_error = reg_dict
    return(reg_dict_with_error)
