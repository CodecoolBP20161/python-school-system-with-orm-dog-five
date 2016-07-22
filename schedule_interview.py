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
    try:
        if len(none_interview) > 0:
            for applicant in Applicant.select().where(Applicant.interview == None):
                applicant.interview = none_interview[i]
                none_interview.remove(none_interview[i])
                i -= 1
                applicant.save()
        else:
            interview_error()
    except IndexError:
        interview_error()


def interview_error():
    print("There are not enough interview-slot!")
    for applicant in Applicant.select().where(Applicant.interview == None):
        print("Applicant who does not have reserved interview: %s - ID: %d" % (applicant.name, applicant.aid))

set_reserved()
reserved_interview_to_applicant()