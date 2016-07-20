from peewee import *

def set_db():
    dbname = input("Database name: ")
    username = input("User name: ")
    db = PostgresqlDatabase(dbname, user=username)
    return db

db = set_db()
