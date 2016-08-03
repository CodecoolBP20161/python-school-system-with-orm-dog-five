from models import *
from mentor import Mentor


class Interview(BaseModel):
    '''This class handles with the interview model/table'''
    iid = PrimaryKeyField()
    day = DateField()
    start_time = TimeField()
    end_time = TimeField()
    reserved = BooleanField(default=False)

    # THIS CODE IS FOR FUTURE WORK
    # DO NOT DELETE!!!
    # @classmethod
    # def set_reserved_2(cls):
    #     reserved_list = list(Applicant.select().where(Applicant.interview != None))
    #     query = cls.select()
    #     for k in query:
    #         if k in reserved_list:
    #             print("Yess")
    #             k.reserved = True
    #             k.save()
    #         else:
    #             print("NO")

    # @classmethod
    # def set_reserved(cls):
    #     reserved_list = list(Applicant.select().where(Applicant.interview is not None))
    #     # for i in Applicant.select().where(Applicant.interview is not None):
    #     #     reserved_list.append(i.interview)
    #     for k in cls.select():
    #         print(k.iid)
    #         if k.iid in reserved_list:
    #             print("OK")
    #             k.reserved = True
    #             k.save()
    #
    #     print(reserved_list)

    # This method uplodes the Interview ID(iid) to the Applicant interview column
    @classmethod
    def reserved_interview_to_applicant(cls):
        from applicant import Applicant

        none_interview = list(cls.select().where(cls.reserved != True))
        i = len(none_interview) - 1
        try:
            if len(none_interview) > 0:
                for applicant in Applicant.select().where(Applicant.interview == None):
                    applicant.interview = none_interview[i]
                    none_interview.remove(none_interview[i])
                    i -= 1
                    applicant.save()
            else:
                Interview.interview_error()
        except IndexError:
            Interview.interview_error()

    # This method shows applicant without interview
    @staticmethod
    def interview_error():
        from applicant import Applicant

        print("There are not enough interview-slot!")
        for applicant in Applicant.select().where(Applicant.interview == None):
            print("Applicant who does not have reserved interview: %s - ID: %d" % (applicant.name, applicant.aid))
