from model.applicant import Applicant


# This function manages the submit function from the /registration route
def register_applicant(reg_dict):
    reg_dict_with_error = Applicant.build_new(reg_dict)
    Applicant.get_closest_school()
    Applicant.update_appl_code()
    return(reg_dict_with_error)