from peewee import *
from model.basemodel import BaseModel
from model.applicant import Applicant
from model.mentor import Mentor
from model.interview_slot import InterviewSlot


class Interview(BaseModel):
    """Assigns interviews to new applicants with mentors"""
    applicant = ForeignKeyField(Applicant, related_name="applicants_id", default=None, null=True)
    mentor = ForeignKeyField(Mentor, related_name="mentors_id", default=None, null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name="interviews_id", default=None, null=True)

    # schedules an interview with error handling
    @classmethod
    def schedule(cls):
        """finds free interviews and assigns applicant and mentor with matching city"""
        a_notin_is = Applicant.select().join(cls, JOIN.LEFT_OUTER).where(cls.applicant_id==None)

        for a in a_notin_is:
            if a.school_cid is not None:
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
