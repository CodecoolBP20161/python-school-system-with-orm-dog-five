from peewee import *
import os

class Connection:
    '''Handles everything related to database connection'''

    # check whether the login file already exits
    @staticmethod
    def check_dsn_txt():
        return os.path.isfile('./login.txt')

    # saves PostgreSQL login data into txt file
    @staticmethod
    def dsn_input():
        dbname = input("Database name: ")
        username = input("User name: ")
        dsn_list = [dbname, username]
        with open('login.txt', 'w') as myfile:
            for word in dsn_list:
                myfile.write(word + '\n')
            print("Login file has been created.")

    @classmethod
    # reads postgresql login data from txt file and defines db
    def db_data(cls):
        with open("login.txt", "r") as myfile:
            lines = myfile.readlines()
            dsn_list = [line.strip("\n") for line in lines]
            dbname, username = dsn_list
            cls.db = PostgresqlDatabase(dbname, user=username)
            return cls.db

    # checks whether the login file already exists and creates connection with PostgreSQL
    @classmethod
    def set_db(cls):
        if cls.check_dsn_txt():
            return cls.db_data()
        else:
            cls.dsn_input()
            return cls.db_data()

    # if there is an error with connecting to PostgreSQL this function provides the option to reenter
    # login data
    @classmethod
    def error_db(cls):
        answer = print('Cannot connect to PostgreSQL. Check whether PostgrSQL is running and reenter login data!')
        cls.dsn_input()
        cls.set_db()

db = Connection.set_db()
