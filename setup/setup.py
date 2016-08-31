from setup.setup_email import ConnectEmail
from setup.setup_database import ConnectDB
from setup.build_data import Build
from setup.example_data import ExampleData


def setup_db_all():
    Build.create_tables()
    Build.upload_data()


def setup_email_all():
    ConnectEmail.set_smtp()
