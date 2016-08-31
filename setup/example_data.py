from peewee import *
from model.basemodel import BaseModel
from model.applicant import Applicant
from model.city import City
from model.closest import Closest
from model.interview import Interview
from model.interview_slot import InterviewSlot
from model.mentor import Mentor
from model.school import School
from datetime import date
from datetime import time

class ExampleData():
    """contains example data"""

    city_list = ['Miskolc',
                 'Budapest',
                 'Kraków',
                 'Székesfehérvár',
                 'Budaörs',
                 'Eger',
                 'Vác',
                 'Győr',
                 'Debrecen',
                 'Sopron',
                 'Pécs']

    applicants_list = [
                      {'name': 'János',
                       'application_code': 161,
                       'home': 2,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Réka',
                       'application_code': None,
                       'home': 1,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'John',
                       'application_code': 234,
                       'home': 4,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Emese',
                       'application_code': 235,
                       'home': 6,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Gergő',
                       'application_code': None,
                       'home': 9,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Tamás',
                       'application_code': 432,
                       'home': 10,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Levente',
                       'application_code': 876,
                       'home': 4,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Anna',
                       'application_code': 712,
                       'home': 3,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Mónika',
                       'application_code': 342,
                       'home': 2,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Noémi',
                       'application_code': 189,
                       'home': 2,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Dániel',
                       'application_code': 195,
                       'home': 8,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Rotáb',
                       'application_code': 196,
                       'home': 10,
                       'school': None,
                       'email': "codecool.dog5@gmail.com"}
                       ]

    mentor_list = [
                    {'name': 'Miki', 'school': 2},
                    {'name': 'Tomi', 'school': 2},
                    {'name': 'Dani', 'school': 2},
                    {'name': 'Attila', 'school': 1},
                    {'name': 'Pali', 'school': 1},
                    {'name': 'Sanyi', 'school': 1},
                    {'name': 'Wladyslaw', 'school': 3}
                    ]

    school_list = [
                  {'name': 'Miskolc',
                   'city': 1},
                  {'name': 'Budapest',
                   'city': 2},
                  {'name': 'Kraków',
                   'city': 3}
                   ]

    closest_list = [
                    {'home': 1, 'school': 1},
                    {'home': 2, 'school': 2},
                    {'home': 3, 'school': 3},
                    {'home': 4, 'school': 2},
                    {'home': 5, 'school': 2},
                    {'home': 6, 'school': 1},
                    {'home': 7, 'school': 2},
                    {'home': 8, 'school': 2},
                    {'home': 9, 'school': 2},
                    {'home': 10, 'school': 2},
                    {'home': 11, 'school': 2}
                    ]

    interview_slot_list = [
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 3
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 3
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 2
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 2
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 2
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 2
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 2
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(15),
                       'end_time': time(16),
                       'location': 1
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(16),
                       'end_time': time(17),
                       'location': 2,
                       'reserved': True
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 1
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(15),
                       'end_time': time(16),
                       'location': 1
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(16),
                       'end_time': time(17),
                       'location': 1
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 1
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(15),
                       'end_time': time(16),
                       'location': 1
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(16),
                       'end_time': time(17),
                       'location': 1
                       },
                      {'day': date(2016, 7, 27),
                       'start_time': time(14),
                       'end_time': time(15),
                       'location': 1
                       }
                       ]

    scheduled_interviews = [{'applicant': 1,
                             'mentor': 2,
                             'interview_slot': 3}]

    # cities table
    @classmethod
    def create_cities(cls):
        for c in cls.city_list:
            city = City.create(name=c)

    # applicants table
    @classmethod
    def create_applicants(cls):
        for a in cls.applicants_list:
            applicant = Applicant.create(name=a['name'],
                                         application_code=a['application_code'],
                                         home=a['home'],
                                         school=a['school'],
                                         email=a['email'])

    # school table
    @classmethod
    def create_school(cls):
        for s in cls.school_list:
            school = School.create(name=s['name'], city=s['city'])

    # closest cities pairing table
    @classmethod
    def create_closest(cls):
        for c in cls.closest_list:
            closest = Closest.create(home=c['home'],
                                     school=c['school'])

    # mentors table
    @classmethod
    def create_mentor(cls):
        for m in cls.mentor_list:
            mentor = Mentor.create(name=m['name'], school=m['school'])

    # interview time slots
    @classmethod
    def create_interview(cls):
        for i in cls.interview_slot_list:
            interview_slot = InterviewSlot.create(day=i['day'],
                                              start_time=i['start_time'],
                                              end_time=i['end_time'],
                                              location=i['location'])

    # scheduled interviews
    @classmethod
    def create_scheduled_interviews(cls):
        for i in cls.scheduled_interviews:
            scheduled_interview = Interview.create(applicant=i['applicant'],
                                                   mentor=i['mentor'],
                                                   interview_slot=i['interview_slot'])
