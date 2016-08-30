from models import *
from mentor import Mentor
from school import School


class Interview(BaseModel):
    '''This class handles with the interview model/table'''
    iid = PrimaryKeyField()
    location = ForeignKeyField(School, related_name="interview_location")
    day = DateField()
    start_time = TimeField()
    end_time = TimeField()
    reserved = BooleanField(default=False)

    def update_to_reserved(self):
        self.reserved = True
        self.save()
