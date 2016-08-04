from models import *
from applicant import Applicant
from city import City
from closest import Closest
from interview import Interview
from mentor import Mentor
from school import School
from datetime import time
from datetime import date


class ExampleData():
    """fills up the database with example data"""

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
                       'home_cid': 2,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Réka',
                       'application_code': None,
                       'home_cid': 1,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'John',
                       'application_code': 234,
                       'home_cid': 4,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Emese',
                       'application_code': 235,
                       'home_cid': 6,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Gergő',
                       'application_code': None,
                       'home_cid': 9,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Tamás',
                       'application_code': 432,
                       'home_cid': 10,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Levente',
                       'application_code': 876,
                       'home_cid': 4,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Anna',
                       'application_code': 712,
                       'home_cid': 3,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Mónika',
                       'application_code': 342,
                       'home_cid': 2,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Noémi',
                       'application_code': 189,
                       'home_cid': 2,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Dániel',
                       'application_code': 195,
                       'home_cid': 8,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"},
                      {'name': 'Rotáb',
                       'application_code': 196,
                       'home_cid': 10,
                       'school_cid': None,
                       'email': "codecool.dog5@gmail.com"}
                       ]

    mentor_list = [
                    {'name': 'Miki', 'school_cid': 2},
                    {'name': 'Tomi', 'school_cid': 2},
                    {'name': 'Dani', 'school_cid': 2},
                    {'name': 'Attila', 'school_cid': 1},
                    {'name': 'Pali', 'school_cid': 1},
                    {'name': 'Sanyi', 'school_cid': 1},
                    {'name': 'Wladyslaw', 'school_cid': 3}
                    ]

    school_list = [
                  {'name': 'Miskolc',
                   'cid': 1},
                  {'name': 'Budapest',
                   'cid': 2},
                  {'name': 'Kraków',
                   'cid': 3}
                   ]

    closest_list = [
                    {'home_cid': 1, 'school_cid': 1},
                    {'home_cid': 2, 'school_cid': 2},
                    {'home_cid': 3, 'school_cid': 3},
                    {'home_cid': 4, 'school_cid': 2},
                    {'home_cid': 5, 'school_cid': 2},
                    {'home_cid': 6, 'school_cid': 1},
                    {'home_cid': 7, 'school_cid': 2},
                    {'home_cid': 8, 'school_cid': 2},
                    {'home_cid': 9, 'school_cid': 2},
                    {'home_cid': 10, 'school_cid': 2},
                    {'home_cid': 11, 'school_cid': 2}
                    ]

    interview_list = [
                      {'day': date(2016, 7, 24),
                       'start_time': time(14),
                       'end_time': time(15)
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(15),
                       'end_time': time(16)
                       },
                      {'day': date(2016, 7, 24),
                       'start_time': time(16),
                       'end_time': time(17)
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(14),
                       'end_time': time(15)
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(15),
                       'end_time': time(16)
                       },
                      {'day': date(2016, 7, 25),
                       'start_time': time(16),
                       'end_time': time(17)
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(14),
                       'end_time': time(15)
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(15),
                       'end_time': time(16)
                       },
                      {'day': date(2016, 7, 26),
                       'start_time': time(16),
                       'end_time': time(17)
                       },
                      {'day': date(2016, 7, 27),
                       'start_time': time(14),
                       'end_time': time(15)
                       }
                       ]

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
                                         home_cid=a['home_cid'],
                                         school_cid=a['school_cid'],
                                         interview=a['interview'],
                                         email=a['email'])

    # school table
    @classmethod
    def create_school(cls):
        for s in cls.school_list:
            school = School.create(name=s['name'], cid=s['cid'])

    # closest cities pairing table
    @classmethod
    def create_closest(cls):
        for c in cls.closest_list:
            closest = Closest.create(home_cid=c['home_cid'],
                                     school_cid=c['school_cid'])

    # mentors table
    @classmethod
    def create_mentor(cls):
        for m in cls.mentor_list:
            mentor = Mentor.create(name=m['name'], school_id=m['school_cid'])

    # interview slots
    @classmethod
    def create_interview(cls):
        for i in cls.interview_list:
            interview_slot = Interview.create(day=i['day'],
                                              start_time=i['start_time'],
                                              end_time=i['end_time'],
                                              mentor_id=i['mentor_id'])
