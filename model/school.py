from peewee import *
from model.basemodel import BaseModel
from model.city import City


class School(BaseModel):
    """city table/model"""
    name = CharField()
    city = ForeignKeyField(City, related_name="school_location")

    @classmethod
    def get_school_list(cls):
        school_list = []
        for school in cls.select():
            school_list.append(school.name)
        return school_list