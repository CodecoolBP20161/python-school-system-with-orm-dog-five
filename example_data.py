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
                        'school_cid': None,
                        'interview': None},
                       {'name': 'Réka',
                        'application_code': None,
                        'home_cid': 1,
                        'school_cid': None,
                        'interview': 2},
                       {'name': 'John',
                        'application_code': 234,
                        'home_cid': 4,
                        'school_cid': None,
                        'interview': 3},
                       {'name': 'Emese',
                        'application_code': 235,
                        'home_cid': 6,
                        'school_cid': None,
                        'interview': 4},
                       {'name': 'Gergő',
                        'application_code': None,
                        'home_cid': 9,
                        'school_cid': None,
                        'interview': 5},
                       {'name': 'Tamás',
                        'application_code': 432,
                        'home_cid': 10,
                        'school_cid': None,
                        'interview': 6},
                       {'name': 'Levente',
                        'application_code': 876,
                        'home_cid': 4,
                        'school_cid': None,
                        'interview': None},
                       {'name': 'Anna',
                        'application_code': 712,
                        'home_cid': 3,
                        'school_cid': None,
                        'interview': None},
                       {'name': 'Mónika',
                        'application_code': 342,
                        'home_cid': 2,
                        'school_cid': None,
                        'interview': None},
                       {'name': 'Noémi',
                        'application_code': 189,
                        'home_cid': 2,
                        'school_cid': None,
                        'interview': None},
                       {'name': 'Dániel',
                        'application_code': 195,
                        'home_cid': 8,
                        'school_cid': None,
                        'interview': None},
                        {'name': 'Rotáb',
                         'application_code': 196,
                         'home_cid': 10,
                         'school_cid': None,
                         'interview': None}
    ]

    for a in applicants_list:
        applicant = Applicant.create(name=a['name'], application_code=a['application_code'], home_cid=a['home_cid'], school_cid=a['school_cid'], interview=a['interview'])


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
                    {'name': 'Miki', 'school_cid': 2},
                    {'name': 'Tomi', 'school_cid': 2},
                    {'name': 'Dani', 'school_cid': 2},
                    {'name': 'Attila', 'school_cid': 1},
                    {'name': 'Pali', 'school_cid': 1},
                    {'name': 'Sanyi', 'school_cid': 1},
                    {'name': 'Wladyslaw', 'school_cid': 3}
    ]
    for m in mentor_list:
        mentor = Mentor.create(name=m['name'], school_id=m['school_cid'])


def create_interview():
    interview_list = [
                      {'day': date(2016, 7, 24),
                       'start': time(14),
                       'end': time(15),
                       'mentor_id': 1},
                      {'day': date(2016, 7, 24),
                       'start': time(15),
                       'end': time(16),
                       'mentor_id': 2},
                      {'day': date(2016, 7, 24),
                       'start': time(16),
                       'end': time(17),
                       'mentor_id': 3},
                      {'day': date(2016, 7, 25),
                       'start': time(14),
                       'end': time(15),
                       'mentor_id': 1},
                      {'day': date(2016, 7, 25),
                       'start': time(15),
                       'end': time(16),
                       'mentor_id': 2},
                      {'day': date(2016, 7, 25),
                       'start': time(16),
                       'end': time(17),
                       'mentor_id': 1},
                      {'day': date(2016, 7, 26),
                       'start': time(14),
                       'end': time(15),
                       'mentor_id': 2},
                      {'day': date(2016, 7, 26),
                       'start': time(15),
                       'end': time(16),
                       'mentor_id': 1},
                      {'day': date(2016, 7, 26),
                       'start': time(16),
                       'end': time(17),
                       'mentor_id': 2},
                      {'day': date(2016, 7, 27),
                       'start': time(14),
                       'end': time(15),
                       'mentor_id': 1},
                      # {'day': date(2016, 7, 27),
                      #  'start': time(15),
                      #  'end': time(16),
                      #  'mentor_id': 3},
                      #   {'day': date(2016, 7, 28),
                      #    'start': time(16),
                      #    'end': time(17),
                      #    'mentor_id': 2},
                      #   {'day': date(2016, 7, 28),
                      #    'start': time(16),
                      #    'end': time(17),
                      #    'mentor_id': 2},
                      #   {'day': date(2016, 7, 28),
                      #    'start': time(16),
                      #    'end': time(17),
                      #    'mentor_id': 2}
    ]
    for i in interview_list:
        interview_slot = Interview.create(day=i['day'], start=i['start'], end=i['end'], mentor_id=i['mentor_id'])


create_cities()

create_school()
create_closest()
create_mentor()
create_interview()
create_applicants()
