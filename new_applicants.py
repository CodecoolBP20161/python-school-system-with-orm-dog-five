# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *

def get_closest_school():
    query = Closest.select(Closest.school_cid).where(Applicant.home_cid == Closest.home_cid)
    for applicant in Applicant.select():
        if applicant.school_cid is None:
            applicant.school_cid = query
            applicant.save()
        else:
            continue

# get_closest_school()
