from peewee import *
from model.basemodel import BaseModel
from model.city import City
from model.school import School
from random import randint


class Applicant(BaseModel):
    """Applicant model/table and data manipulation related to it"""
    name = CharField()
    application_code = IntegerField(null=True, unique=True)
    home = ForeignKeyField(City, related_name="appl_home")
    school = ForeignKeyField(School, related_name="appl_school", null=True)
    # in real life this should be unique, but we send all e-mails to the same e-mail account in our test data
    email = CharField()
    sent_application_email = BooleanField(default=False)
    sent_interview_email = BooleanField(default=False)
    code_set = set()


    # assigns closest school for applicant
    @classmethod
    def get_closest_school(cls):
        query = Closest.select(Closest.school).where(cls.home == Closest.home)
        for applicant in cls.select():
            if applicant.school is None:
                applicant.school = query
                applicant.save()
            else:
                continue


    # collects appl codes into a set
    @classmethod
    def read_codes(cls):
        code_set = set()
        for appl_record in cls.select():
            code_set.add(appl_record.application_code)
        return(code_set)


    # assigns closest school for applicant
    @classmethod
    def update_appl_code(cls):
        cls.code_set = cls.read_codes()
        for appl in cls.select().where(cls.application_code == None):
            appl.generate_code()
            appl.save()


    # generates unique code for applicant record
    def generate_code(self):
        while True:
            if self.application_code not in self.code_set:
                break
            self.application_code = randint(100, 999)
        self.code_set.add(self.application_code)


    # saves applicant as record from dict input
    @classmethod
    def add_applicant(cls, reg_dict):
        applicant = cls.create(name=reg_dict['name'],
                               home=reg_dict['home'],
                               email=reg_dict['email'])


    # checks user input in dictionary and returns with error
    def check_record():
        pass
