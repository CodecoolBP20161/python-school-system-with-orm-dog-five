from flask import Flask, render_template, url_for, redirect, request
from controller.business import register_applicant



app = Flask(__name__)


@app.route('/')
@app.route('/registration', methods=['GET'])
def reg_form():
    return render_template('registration.html', name_text='')


@app.route('/registration', methods=['POST'])
def submit_form():
    reg_data = dict(request.form)
    is_valid = register_applicant(reg_data)
    name_error = ''
    email_error = ''
    address_error = ''

    if is_valid is None:
         return render_template('registration_saved.html')
    else:
        errors = list(is_valid['error'])
        while len(errors) > 0:
            for error in errors:
                if error == 'name':
                    name_error= '*'
                    errors.remove(error)
                elif error == 'email':
                    email_error= '*'
                    errors.remove(error)
                elif error == 'address':
                    address_error = '*'
                    errors.remove(error)
        return render_template('registration.html', name_text=is_valid['name'],
                                                     email_text=is_valid['email'],
                                                     address_text=is_valid['address'],
                                                     name_error=name_error,
                                                     email_error=email_error,
                                                     address_error=address_error)

if __name__ == '__main__':
    app.run(debug=True)