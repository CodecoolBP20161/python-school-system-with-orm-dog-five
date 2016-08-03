from models import *
from mentor import Mentor
from interview import Interview


class InterviewSlot(BaseModel):
    id = PrimaryKeyField()
    mentor_id = ForeignKeyField(Mentor, related_name="mentors_id")
    interview_id = ForeignKeyField(Interview, related_name="interviews_id")