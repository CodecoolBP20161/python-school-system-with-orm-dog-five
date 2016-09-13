from setup.setup_email import ConnectEmail
from setup.setup_database import ConnectDB
from setup.build_data import Build
from routes.server import app


def setup_db_all():
    db = ConnectDB.build_from_file().db
    Build.create_tables(db)
    Build.upload_data()


def setup_email_all():
    smtp_server = ConnectEmail.build_from_file()


def start_web_server():
    app.run()
