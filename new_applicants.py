# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *
from random import randint


def get_closest_school():
    query = Closest.select(Closest.school_cid).where(Applicant.home_cid == Closest.home_cid)
    for applicant in Applicant.select():
        if applicant.school_cid is None:
            applicant.school_cid = query
            applicant.save()
        else:
            continue


def read_codes(Applicant):
    code_set = set()
    for appl_record in Applicant.select():
        code_set.add(appl_record.application_code)
    try:
        code_set.remove(None)
    except KeyError:
        pass
    return(code_set)


def update_appl_code(Applicant):
    code_set = read_codes(Applicant)
    for appl_record in Applicant.select():
        while True:
            if appl_record.application_code in code_set:
                break
            appl_record.application_code = randint(100, 999)
        code_set.add(appl_record.application_code)
        appl_record.save()


get_closest_school()
update_appl_code(Applicant)
