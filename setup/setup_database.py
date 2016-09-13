from peewee import *
import json
import os


class ConnectDB:
    '''Handles everything related to database connection'''

    __default = {'dbname': 'postgres', 'username': 'postgres'}

    def __init__(self, dbname, username):
        self.db = PostgresqlDatabase(dbname, user=username)

    @classmethod
    def build_from_file(cls):
        if os.path.isfile('setup/login.json'):
            with open('setup/login.json', 'r') as infile:
                data = json.load(infile)
        else:
            data = cls.get_user_data()
        return cls(**data)

    @classmethod
    def get_user_data(cls):
        choice = input('Use default? Press (y) for yes.\n')
        if choice == 'y':
            data = cls.__default
        else:
            dbname = input("Database name: ")
            username = input("User name: ")
            data = {'dbname': dbname, 'username': username}
        with open('setup/login.json', 'w') as outfile:
            json.dump(data, outfile)
        return data
