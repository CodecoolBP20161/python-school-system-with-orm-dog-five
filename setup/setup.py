from setup.setup_email import ConnectEmail
from setup.build_data import Build
from routes.server import app
from model.applicant import Applicant
from model.interview import Interview


def setup_db_all():
    Build.create_tables()
    Build.upload_data()


def setup_email_all():
    ConnectEmail.set_smtp()


def start_web_server():
    app.run()


def process_new_applicant():
    Applicant.get_closest_school()
    Applicant.update_appl_code()


def process_acceptance():
    Interview.schedule()
