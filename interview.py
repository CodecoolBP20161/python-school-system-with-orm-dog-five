from models import *
from mentor import Mentor
from applicant import Applicant


class Interview(BaseModel):
    iid = PrimaryKeyField()
    day = DateField()
    start_time = TimeField()
    end_time = TimeField()
    mentor_id = ForeignKeyField(Mentor, related_name='mentor_interview')
    reserved = BooleanField(default=False)
    print("OK")
    @classmethod
    def set_reserved(cls):
        reserved_list = []
        for i in Applicant.select().where(Applicant.interview != None):
            reserved_list.append(i.interview)
        query = cls.select(cls.iid)
        for k in reserved_list:
            if k in query:
                k.reserved = True
                print("OK")
                k.save()
                print("OK")
    @classmethod
    def reserved_interview_to_applicant(cls):
        none_interview = list(cls.select().where(cls.reserved != True))
        print("ELSŐ", len(none_interview))
        i = len(none_interview) - 1
        try:
            if len(none_interview) > 0:
                for applicant in Applicant.select().where(Applicant.interview == None):
                    applicant.interview = none_interview[i]
                    none_interview.remove(none_interview[i])
                    i -= 1
                    applicant.save()
                print("MÁSODIK", len(none_interview))
            else:
                Interview.interview_error()
        except IndexError:
            Interview.interview_error()

    @staticmethod
    def interview_error():
        print("There are not enough interview-slot!")
        for applicant in Applicant.select().where(Applicant.interview == None):
            print("Applicant who does not have reserved interview: %s - ID: %d" % (applicant.name, applicant.aid))