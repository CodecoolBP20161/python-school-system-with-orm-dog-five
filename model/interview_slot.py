from peewee import *
from model.basemodel import BaseModel
from model.school import School


class InterviewSlot(BaseModel):
    '''This class handles with the interview model/table'''
    location = ForeignKeyField(School, related_name="interview_location")
    day = DateField()
    start_time = TimeField()
    end_time = TimeField()
    reserved = BooleanField(default=False)

    def update_to_reserved(self):
        self.reserved = True
        self.save()
