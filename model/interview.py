from peewee import *
from model.basemodel import BaseModel
from model.applicant import Applicant
from model.mentor import Mentor
from model.interview_slot import InterviewSlot


class Interview(BaseModel):
    """Assigns interviews to new applicants with mentors"""
    applicant = ForeignKeyField(Applicant, related_name='applicants_id', default=None, null=True)
    mentor = ForeignKeyField(Mentor, related_name='mentors_id', default=None, null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name="interviews_id", default=None, null=True)

    # schedules an interview with error handling
    @classmethod
    def schedule(cls):
        """finds free interviews and assigns applicant and mentor with matching city"""
        a_notin_is = Applicant.select().join(cls, JOIN.LEFT_OUTER).where(cls.applicant==None)

        for a in a_notin_is:
            if a.school is not None:
                try:
                    mentor = Mentor.get(Mentor.school==a.school)
                    interview_slot = InterviewSlot.get(InterviewSlot.location==a.school)
                except Mentor.DoesNotExist:
                    return 'No available mentor.'
                except InterviewSlot.DoesNotExist:
                    return 'No available interview time slot.'
                cls.insert(applicant=a.id, mentor=mentor.id, interview_slot=interview_slot.id).execute()
                interview_slot.update_to_reserved()
            else:
                return 'Assign closest school to applicants first.'

