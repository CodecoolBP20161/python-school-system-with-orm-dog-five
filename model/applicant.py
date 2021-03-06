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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.registration_error_set = set()
        self.code_set = set()

    #
    # process new applicant
    #
    @classmethod
    def build_new(cls, reg_dict):
        applicant = cls.convert_raw_data(reg_dict)
        applicant.generate_code()
        applicant.validate()
        if applicant.registration_error_set == set():
            applicant.save()
            return applicant
        else:
            return applicant

    @classmethod
    def convert_raw_data(cls, reg_dict):
        try:
            home_city = City.get(name=reg_dict['home'])
            home_id = home_city.id
        except City.DoesNotExist:
            home_id = None
        try:
            school = School.get(name=reg_dict['school'])
            school_id = school.id
        except School.DoesNotExist:
            school_id = None
        applicant = cls(name=reg_dict['name'],
                        home=home_id,
                        email=reg_dict['email'],
                        school=school_id)
        return applicant

    #
    # validation
    #
    def validate(self):
        self.check_name()
        self.check_home()
        self.check_school()
        self.check_email()

    def check_name(self):
        if ' ' not in self.name:
            self.registration_error_set.add('name')

    def check_home(self):
        if self.home is None:
            self.registration_error_set.add('home')

    def check_school(self):
        if self.school is None:
            self.registration_error_set.add('school')

    def check_email(self):
        data = Applicant.select()
        email_list = []
        for i in data:
            email_list.append(i.email)
        if ('@' not in self.email) or ('.' not in self.email) or self.email in email_list:
            self.registration_error_set.add('email')

    #
    # application code
    #
    @classmethod
    def read_codes(cls):
        code_set = set()
        for appl_record in cls.select():
            code_set.add(appl_record.application_code)
        return code_set

    # call after creating instance to generate a code for that instance
    def generate_code(self):
        self.code_set = self.read_codes()
        while True:
            if self.application_code not in self.code_set:
                break
            self.application_code = randint(1000, 9999)
        self.code_set.add(self.application_code)

    #
    # email
    #
    @property
    def new_app_email(self):
        msg_data = {}
        msg_data['body'] = 'Hi ' + str(self.name) + ","\
                       + "\n\nWe received your application to Codecool "+ str(self.school.name) + "."\
                       + "\nYour application code is " + str(self.application_code) + "." \
                       + "\nYou can log in with your e-mail address using your application code as password." \
                       + "\n\nRegards,\nCodecool Team"
        msg_data['subject'] = 'Welcome'
        msg_data['to'] = str(self.email)
        msg_data['type'] = 'newreg'
        return msg_data

    def new_app_sent(self):
        self.sent_application_email = True
        self.save()

    #
    # login
    #
    @classmethod
    def get_login(cls, password):
        try:
            applicant = cls.get(application_code=password)
            data = {'email':applicant.email, 'password':str(applicant.application_code), 'name':applicant.name}
        except Applicant.DoesNotExist:
            data = {'email':None, 'password':None, 'name':None}
        except ValueError:
            data = {'email':None, 'password':None, 'name':None}
        return data