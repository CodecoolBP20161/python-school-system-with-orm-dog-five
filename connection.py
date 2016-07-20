from peewee import *
import os


def check_dsn_txt():
    return os.path.isfile('./login.txt')


def dsn_input():
    dbname = input("Database name: ")
    username = input("User name: ")
    dsn_list = [dbname, username]
    with open('login.txt', 'w') as myfile:
        for word in dsn_list:
            myfile.write(word + '\n')
        print("Login file has been created.")


def db_data():
    with open("login.txt", "r") as myfile:
        lines = myfile.readlines()
        dsn_list = [line.strip("\n") for line in lines]
        dbname, username = dsn_list
        db = PostgresqlDatabase(dbname, user=username)
        return db


def set_db():
    if check_dsn_txt():
        answer = input("Login data already exists. Do you want to reenter login data? (Y/n) ")
        if answer.lower() == "y":
            dsn_input()
            return db_data()
        elif answer.lower() == 'n':
            return db_data()
        else:
            print("Not a valid answer.")
    else:
        dsn_input()
        return db_data()

db = set_db()
