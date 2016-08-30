from setup.setup_email import ConnectEmail
from setup.setup_database import ConnectDB
from setup.build_data import Build

def setup_db_all():
    Build.create_tables()
    # we need new example data to use this
    # Build.upload_data()

def setup_email_all():
    pass
