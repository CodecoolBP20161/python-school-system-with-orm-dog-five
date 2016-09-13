from setup.setup_email import ConnectEmail
from setup.build_data import Build
from routes.server import app


def setup_db_all():
    Build.create_tables()
    Build.upload_data()


def setup_email_all():
    ConnectEmail.setup_initialize()


def start_web_server():
    app.run()

