from peewee import *
from models import BaseModel
from random import randint
from closest import Closest
from city import City
from interview import Interview


class Applicant(BaseModel):
    """Applicant model/table and data manipulation related to it"""
    aid = PrimaryKeyField()
    name = CharField()
    application_code = IntegerField(null=True, unique=True)
    home_cid = ForeignKeyField(City, related_name="appl_home")
    school_cid = ForeignKeyField(City, related_name="appl_school", null=True)
    interview = ForeignKeyField(Interview, related_name="interview_id", null=True, unique=True)
    # in real life this should be unique, but we send all e-mails to the same e-mail account in our test data
    email = CharField()
    sent_email = BooleanField(default=False)
    code_set = set()

    # assigns closest school for applicant
    @classmethod
    def get_closest_school(cls):
        query = Closest.select(Closest.school_cid).where(cls.home_cid == Closest.home_cid)
        for applicant in cls.select():
            if applicant.school_cid is None:
                applicant.school_cid = query
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

    @classmethod
    def is_application_code(cls):
        app_has_appcode = cls.select().where(cls.application_code != None)
        if len(app_has_appcode) >= 1:
            return True
        else:
            return False

    @classmethod
    def is_school_cid(cls):
        app_has_school_cid = cls.select().where(cls.school_cid != None)
        if len(app_has_school_cid) >= 1:
            return True
        else:
            return False


    @classmethod
    def applicants_without_app_code(cls):
        applicants = cls.select().where(cls.application_code == None)
        if len(applicants) != 0:
            return applicants

    @classmethod
    def applicants_without_school(cls):
        applicants = cls.select().where(cls.school_cid == None)
        if len(applicants) != 0:
            return applicants

    # gets the city, the name and the email address of those applicants, who got no e-mail yet
    @classmethod
    def to_send_email(cls):
        data_list = []
        querry = cls.select().where(cls.sent_email == False and cls.application_code != None and cls.school_cid != None)
        if querry.count() != 0:
            for record in querry:
                city_record = City.get(City.cid == record.school_cid)
                data_list.append({'email': record.email,
                                  'name': record.name,
                                  'ap_code': record.application_code,
                                  'city': city_record.name,
                                  'aid': record.aid})
                record.sent_email = True
                record.save()
                return data_list
        else:
            print("Can't send email to everyone.")
            return []
