from flask import Flask, render_template, url_for, redirect, request
from controller.business import register_applicant


app = Flask(__name__)


@app.route('/')
@app.route('/registration', methods=['GET'])
def reg_form():
    reg_data_valid = {}
    return render_template('registration.html', reg_data_valid=reg_data_valid)


@app.route('/registration', methods=['POST'])
def submit_form():
    reg_data = request.form
    reg_dict = {}
    for elem in reg_data:
        reg_dict.update({elem: reg_data[elem]})
    reg_data_valid = register_applicant(reg_dict)

    if reg_data_valid is None:
        return render_template('registration_saved.html')
    else:
        return render_template('registration.html', reg_data_valid=reg_data_valid)

if __name__ == '__main__':
    app.run(debug=True)
