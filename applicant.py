# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from peewee import *
from models import *
from random import randint


class Applicant(BaseModel):
    aid = PrimaryKeyField()
    name = CharField()
    application_code = IntegerField(null=True, unique=True)
    home_cid = ForeignKeyField(City, related_name="appl_home")
    school_cid = ForeignKeyField(City, related_name="appl_school", null=True)
    interview = ForeignKeyField(Interview, related_name='appl_interview', null=True, default=None)
    code_set = set()


    @classmethod
    def get_closest_school(cls):
        query = Closest.select(Closest.school_cid).where(cls.home_cid == Closest.home_cid)
        for applicant in cls.select():
            if applicant.school_cid is None:
                applicant.school_cid = query
                applicant.save()
            else:
                continue


    @classmethod
    def read_codes(cls):
        code_set = set()
        for appl_record in cls.select():
            code_set.add(appl_record.application_code)
        return(code_set)


    @classmethod
    def update_appl_code(cls):
        cls.code_set = cls.read_codes()
        for appl in cls.select().where(cls.application_code == None):
            appl.generate_code()
            appl.save()


    def generate_code(self):
        while True:
            if self.application_code not in self.code_set:
                break
            self.application_code = randint(100, 999)
        self.code_set.add(self.application_code)
