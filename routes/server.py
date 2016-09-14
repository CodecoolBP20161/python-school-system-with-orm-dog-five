from flask import Flask, render_template, url_for, redirect, request
from controller.business import register_applicant
from model.school import School


app = Flask(__name__)


@app.route('/')
@app.route('/registration', methods=['GET'])
def reg_form():
    school_list = School.get_school_list()
    reg_data_valid = {}
    return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list)


@app.route('/registration', methods=['POST'])
def submit_form():
    school_list = School.get_school_list()
    reg_data = request.form
    reg_dict = {}
    for elem in reg_data:
        reg_dict.update({elem: reg_data[elem]})
    reg_dict['home'] = 'Budapest'
    reg_data_valid = register_applicant(reg_dict)

    if reg_data_valid is None:
        return render_template('registration_saved.html')
    else:
        return render_template('login.html', reg_data_valid=reg_data_valid, school_list=school_list)

@app.route('/admin', methods=['GET'])
def admin_panel():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)

