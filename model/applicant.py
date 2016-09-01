from peewee import *
from model.basemodel import BaseModel
from model.city import City
from model.school import School
from random import randint


class Applicant(BaseModel):
    """Applicant model/table and data manipulation related to it"""
    name = CharField()
    application_code = IntegerField(null=True, unique=True)
    home = ForeignKeyField(City, related_name="appl_home", null=True)
    school = ForeignKeyField(School, related_name="appl_school", null=True)
    # in real life this should be unique, but we send all e-mails to the same e-mail account in our test data
    email = CharField()
    sent_application_email = BooleanField(default=False)
    sent_interview_email = BooleanField(default=False)
    code_set = set()
    registration_error_set = set()

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
        return code_set

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

    @classmethod
    def convert_raw_data(cls, reg_dict):
        try:
            home_city = City.get(name=reg_dict['home'])
            home_id = home_city.id
        except City.DoesNotExist:
            home_id = None
        applicant = cls(name=reg_dict['name'],
                        home=home_id,
                        email=reg_dict['email'])
        return applicant

    def validate(self):
        self.registration_error_set = set()
        self.check_name()
        self.check_home()
        self.check_email()

    def check_name(self):
        if ' ' not in self.name:
            self.registration_error_set.add('name')

    def check_home(self):
        if self.home is None:
            self.registration_error_set.add('home')

    def check_email(self):
        if ('@' not in self.email) or ('.' not in self.email):
            self.registration_error_set.add('email')

    @classmethod
    def build_new(cls, reg_dict):
        applicant = cls.convert_raw_data(reg_dict)
        applicant.validate()
        if applicant.registration_error_set == set():
            applicant.save()
            return None
        else:
            reg_dict['error'] = applicant.registration_error_set
            return reg_dict
