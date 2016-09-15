from flask import Flask, render_template, url_for, redirect, request, flash, session
from controller.business import register_applicant, get_login
from model.school import School
from model.applicant import Applicant
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/about', methods=['GET'])
def about_us():
    return render_template('about.html')


@app.route('/services', methods=['GET'])
def our_services():
    return render_template('services.html')


@app.route('/contacts', methods=['GET'])
def contact_us():
    return render_template('contacts.html')


@app.route('/')
def index():
    school_list = School.get_school_list()
    reg_data_valid = {}
    error = ''
    return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list, error=error)


@app.route('/registration', methods=['GET'])
def reg_form():
    return redirect(url_for('index'))


@app.route('/registration', methods=['POST'])
def submit_form():
    school_list = School.get_school_list()
    reg_data = request.form
    reg_dict = {}
    error = ''
    for elem in reg_data:
        reg_dict.update({elem: reg_data[elem]})
    reg_dict['home'] = 'Budapest'
    reg_data_valid = register_applicant(reg_dict)

    if reg_data_valid is None:
        return render_template('registration_saved.html')
    else:
        return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list, error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    reg_data_valid = {}
    school_list = School.get_school_list()

    if request.method == 'POST':
        data = get_login(request.form['password'])
        print(request.form['password'])

        if data['password'] and data['email'] == request.form['email'].strip():
            session['password'] = data['password']
            session['email'] = data['email']
            session['logged_in'] = True
            return render_template('profile.html', name=data['name'])
        else:
            error = 'Invalid password or e-mail'

    return render_template('login.html', reg_data_valid=reg_data_valid, school_list= school_list, error=error)


@app.route('/profile', methods=['GET', 'POST'])
def show_profile():
    if 'password' in session:
        user = Applicant.select().where(Applicant.email==session['email']).get()
        return render_template('profile.html', name=user.name)
    else:
        return redirect(url_for('index'))


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('password', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/admin', methods=['GET'])
def admin_panel():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)

