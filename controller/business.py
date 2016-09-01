from model.applicant import Applicant


# This function manages the submit function from the /registration route
def register_applicant(reg_dict):
    reg_dict_with_error = Applicant.validate(reg_dict)
    return(reg_dict_with_error)
