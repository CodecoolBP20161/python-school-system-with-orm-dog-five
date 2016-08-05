from models import *
from mentor import Mentor
from interview import Interview
from applicant import Applicant
from mentor import Mentor


class InterviewSlot(BaseModel):
    """Assigns interviews to new applicants with mentors"""
    id = PrimaryKeyField()
    applicant_id = ForeignKeyField(Applicant, related_name="applicants_id", default=None, null=True)
    mentor_id = ForeignKeyField(Mentor, related_name="mentors_id", default=None, null=True)
    interview_id = ForeignKeyField(Interview, related_name="interviews_id", default=None, null=True)
    sent_interview = BooleanField(default=False)

    # schedules an interview with error handling
    @classmethod
    def schedule(cls):
        """finds free interviews and assigns applicant and mentor with matching city"""
        a_notin_is = Applicant.select().join(cls, JOIN.LEFT_OUTER).where(cls.applicant_id==None)

        for a in a_notin_is:
            if a.school_cid != None:
                try:
                    mentor = Mentor.get(Mentor.school_id==a.school_cid)
                    interview = Interview.get(Interview.location==a.school_cid)
                except Mentor.DoesNotExist:
                    print('No available mentor.')
                    break
                except Interview.DoesNotExist:
                    print('No available interview time slot.')
                    break
                cls.insert(applicant_id=a.aid, mentor_id=mentor.mid, interview_id=interview.iid).execute()
                interview.update_to_reserved()
            else:
                print('Assign closest school to applicants first.')
                break


    @classmethod
    def set_email_to_sent(cls):
        cls.sent_interview = True


    @classmethod
    def get_everything(cls):
        '''finds applicants name, e-mail, mentors name and a free interview slot which is not reserved
            sends email to applicants to didn't get one earlier'''
        data_list = []
        for applicant in cls.select(Applicant,Mentor,Interview,InterviewSlot).join(Applicant, on=(cls.applicant_id == Applicant.aid)).join(Mentor, on=(cls.mentor_id == Mentor.mid)).join(Interview, on=(cls.interview_id == Interview.iid)).where(cls.sent_interview == False):
            data_list.append({'applicant_name': Applicant.name,
                              'applicant_email': Applicant.email,
                              'mentor_name': Mentor.name,
                              'interview_start': Interview.start_time
                              })
            applicant.sent_interview = True
            applicant.save()
        return data_list

InterviewSlot.get_everything()
