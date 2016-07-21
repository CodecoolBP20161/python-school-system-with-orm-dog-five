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
                        'home': 2},
                       {'name': 'Réka',
                        'application_code': none,
                        'home': 1},
                       {'name': 'John',
                        'application_code': 234,
                        'home': 4},
                       {'name': 'Emese',
                        'application_code': 234,
                        'home': 6},
                       {'name': 'Gergő',
                        'application_code': none,
                        'home': 9},
                       {'name': 'Tamás',
                        'application_code': 432,
                        'home': 10},
                       {'name': 'Levente',
                        'application_code': 876,
                        'home': 4},
                       {'name': 'Anna',
                        'application_code': 712,
                        'home': 3},
                       {'name': 'Mónika',
                        'application_code': 342,
                        'home': 2},
                       {'name': 'Noémi',
                        'application_code': 189,
                        'home': 2},
                       {'name': 'Dániel',
                        'application_code': 195,
                        'home': 8},
    ]

    for a in applicants_list:
        applicant = Applicant.create(name=a['name'], application_code=a['application_code'], home=a['home'])


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

create_cities()
create_applicants()
create_school()
create_closest()
