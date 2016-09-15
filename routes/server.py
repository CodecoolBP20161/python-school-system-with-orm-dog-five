from flask import Flask, render_template, url_for, redirect, request, flash, session
from controller.business import register_applicant, get_login, show_table
from model.school import School
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
@app.route('/registration', methods=['GET'])
def reg_form():
    school_list = School.get_school_list()
    reg_data_valid = {}
    error = ''
    return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list, error=error)


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
    data = get_login(request.form['password'])
    session['email'] = data['email']
    session['password'] = data['password']

    if request.method == 'POST':
        if request.form['email'] != session['email']:
            error = 'Invalid password or e-mail'
        elif request.form['password'] != session['password']:
            error = 'Invalid password or e-mail'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('profile.html', name=data['name'])
    return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list, error=error)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('reg_form'))


@app.route('/admin/e-mail-log', methods=['GET'])
def admin_dashboard():
    email_list = enumerate(show_table())
    return render_template('admin.html', email_list=email_list)

if __name__ == '__main__':
    app.run(debug=True)

