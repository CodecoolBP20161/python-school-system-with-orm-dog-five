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
                        'application_code': 653,
                        'home': 1},
                       {'name': 'John',
                        'application_code': 234,
                        'home': 4},
                       {'name': 'Emese',
                        'application_code': 234,
                        'home': 6},
                       {'name': 'Gergő',
                        'application_code': 893,
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
                    'CID': 1},
                   {'name': 'Budapest',
                    'CID': 2},
                   {'name': 'Kraków',
                    'CID': 3}
    ]
    for s in school_list:
        school = School.create(name=s['name'], CID=s['CID'])


def create_closest():
    closest_list = [
                    {'Home_CID': 1, 'School_CID': 1},
                    {'Home_CID': 2, 'School_CID': 2},
                    {'Home_CID': 3, 'School_CID': 3},
                    {'Home_CID': 4, 'School_CID': 2},
                    {'Home_CID': 5, 'School_CID': 2},
                    {'Home_CID': 6, 'School_CID': 1},
                    {'Home_CID': 7, 'School_CID': 2},
                    {'Home_CID': 8, 'School_CID': 2},
                    {'Home_CID': 9, 'School_CID': 2},
                    {'Home_CID': 10, 'School_CID': 2},
                    {'Home_CID': 11, 'School_CID': 2}
     ]
    for c in closest_list:
        closest = Closest.create(Home_CID=c['Home_CID'], School_CID=c['School_CID'])

create_cities()
create_applicants()
create_school()
create_closest()
