from models import *


def set_reserved():
    reserved_list = []
    for i in Applicant.select().where(Applicant.interview != None):
        reserved_list.append(i.interview)
    query = Interview.select(Interview.iid)
    for k in reserved_list:
        if k in query:
            k.reserved = True
            k.save()


def reserved_interview_to_applicant():
    none_interview = list(Interview.select().where(Interview.reserved != True))
    i = len(none_interview)-1
    for applicant in Applicant.select().where(Applicant.interview == None):
        applicant.interview = none_interview[i]
        i -= 1
        applicant.save()

    print(none_interview)
set_reserved()
reserved_interview_to_applicant()