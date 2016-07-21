# This script can generate example data for "City" and "InterviewSlot" models.

from models import *


def create_cities():
    city_list = ['Miskolc', 'Budapest', 'Kraków', 'Székesfehérvár', 'Budaörs', 'Eger', 'Vác', 'Győr', 'Debrecen', 'Sopron', 'Pécs']
    for c in city_list:
        city = City.create(name=c)


def create_applicants():
    applicants_list = [
                       {'name': 'János',
                        'application_code': 161,
                        'home_cid': 2,
                        'school_cid': None},
                       {'name': 'Réka',
                        'application_code': None,
                        'home_cid': 1,
                        'school_cid': None},
                       {'name': 'John',
                        'application_code': 234,
                        'home_cid': 4,
                        'school_cid': None},
                       {'name': 'Emese',
                        'application_code': 235,
                        'home_cid': 6,
                        'school_cid': None},
                       {'name': 'Gergő',
                        'application_code': None,
                        'home_cid': 9,
                        'school_cid': None},
                       {'name': 'Tamás',
                        'application_code': 432,
                        'home_cid': 10,
                        'school_cid': None},
                       {'name': 'Levente',
                        'application_code': 876,
                        'home_cid': 4,
                        'school_cid': None},
                       {'name': 'Anna',
                        'application_code': 712,
                        'home_cid': 3,
                        'school_cid': None},
                       {'name': 'Mónika',
                        'application_code': 342,
                        'home_cid': 2,
                        'school_cid': None},
                       {'name': 'Noémi',
                        'application_code': 189,
                        'home_cid': 2,
                        'school_cid': None},
                       {'name': 'Dániel',
                        'application_code': 195,
                        'home_cid': 8,
                        'school_cid': None},
    ]

    for a in applicants_list:
        applicant = Applicant.create(name=a['name'], application_code=a['application_code'], home_cid=a['home_cid'], school_cid=a['school_cid'])


def create_school():
    school_list = [
                   {'name': 'Miskolc',
                    'cid': 1},
                   {'name': 'Budapest',
                    'cid': 2},
                   {'name': 'Kraków',
                    'cid': 3}
    ]
    for s in school_list:
        school = School.create(name=s['name'], cid=s['cid'])


def create_closest():
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
    for c in closest_list:
        closest = Closest.create(home_cid=c['home_cid'], school_cid=c['school_cid'])


def create_mentor():
    mentor_list = [
        {'mid': 1, 'name': 'Miki', 'school_cid': 2}
        {'mid': 2, 'name': 'Tomi', 'school_cid': 2}
        {'mid': 3, 'name': 'Dani', 'school_cid': 2}
        {'mid': 4, 'name': 'Attila', 'school_cid': 1}
        {'mid': 5, 'name': 'Pali', 'school_cid': 1}
        {'mid': 6, 'name': 'Sanyi', 'school_cid': 1}
        {'mid': 7, 'name': 'Wladyslaw', 'school_cid': 3}
    ]
    for m in mentor_list:
        mentor = Mentor.create(mid=m['mid'], name=m['name'], school_cid=m['school_id'])


create_cities()
create_applicants()
create_school()
create_closest()
create_mentor()