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
