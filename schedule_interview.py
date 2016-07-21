from models import *


def check_has_interview():
    query = Interview.select(Interview.iid)
    for i in Applicant.select():
        if i.interview == None:
            i.interview = query
            i.save()
            print(i.interview)


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
    none_interview = []
    for i in Interview.select().where(Interview.reserved != True):
        none_interview.append(i.iid)
    for k in none_interview:
        for applicant in Applicant.select().where(Applicant.interview == None):
            applicant.interview = k
            applicant.save()
            print("OK")
            continue
        else:
            continue
    print(none_interview)


#check_has_interview()
set_reserved()
reserved_interview_to_applicant()