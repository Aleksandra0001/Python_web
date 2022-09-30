from flask import render_template, Blueprint, make_response, redirect, url_for, request, session

from personal_app.repository import users

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/')
def base():
    return render_template('base.html')


@auth.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        users.create_user(username, email, password)
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') == 'on' else False
        user = users.login(email, password)

        if user is None:
            return redirect(url_for('auth.register'))

        session['username'] = {'username': user.username, 'id': user.id}
        response = make_response(redirect(url_for('contacts.contacts')))

        if remember:
            pass
        return response

    return render_template('auth/login.html')


@auth.route('/logout', strict_slashes=False)
def logout():
    response = make_response(redirect(url_for('auth.login')))
    # response.set_cookie('username', '', expires=-1)

    return response
