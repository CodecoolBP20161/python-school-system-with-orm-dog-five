from peewee import *
from models import BaseModel
from school import School

class Mentor(BaseModel):
    """Mentor related data and functions"""
    mid = PrimaryKeyField()
    name = CharField()
    school_id = ForeignKeyField(School, related_name='mentors_school')
    email = CharField()

    # gets info to make interview e-mail
    # updates sent_interview_email column to True
    @classmethod
    def to_mentor_interview_msg(cls):
        from applicant import Applicant
        from interview import Interview
        from interview_slot import InterviewSlot
        data_list = []
        querry = Applicant.select().join(InterviewSlot)
        if querry.count() == 0:
            raise StopIteration
        for record in querry:
            try:
                mentor = Mentor.select().join(InterviewSlot).where(InterviewSlot.applicant_id==record.aid).get()
                interview = Interview.select().join(InterviewSlot).where(InterviewSlot.applicant_id==record.aid).get()
            except Mentor.DoesNotExist:
                print('No available mentor.')
                break
            except Interview.DoesNotExist:
                print('No available interview time slot.')
                break
            data_list.append({'email': mentor.email,
                              'm_name': mentor.name,
                              'ap_name': record.name,
                              'city': interview.location.name,
                              'date': interview.day,
                              'start_time': interview.start_time,
                              'end_time': interview.end_time
                              })
        return data_list
