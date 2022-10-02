import uuid
from datetime import datetime, timedelta

from flask import render_template, Blueprint, make_response, redirect, url_for, request, session, flash

from personal_app.repository import users

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.before_request
def before_func():
    user = True if 'username' in session else False
    if not user:
        token_user = request.cookies.get('username')
        if token_user:
            user = users.get_user_by_token(token_user)
            if user:
                session['username'] = {"username": user.username, "id": user.id}


@auth.route('/')
def base():
    user = True if 'username' in session else False
    print('AUTH:', user)
    return render_template('base.html', auth=user)


@auth.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    user = True if 'username' in session else False
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        users.create_user(username, email, password)
        flash('Welcome to the Phonebook!')
        return redirect(url_for('auth.login'))

    flash('Please, register')
    return render_template('auth/register.html', auth=user)


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    user = True if 'username' in session else False
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') == 'on' else False
        user = users.login(email, password)

        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('auth.register'))

        session['username'] = {'username': user.username, 'id': user.id}
        response = make_response(redirect(url_for('contacts.contacts')))

        if remember:
            token = str(uuid.uuid4())
            expire_data = datetime.now() + timedelta(days=60)
            response.set_cookie('username', token, expires=expire_data)
            users.set_token(user, token)
        return response
    if user:
        return redirect(url_for('contacts.contacts'))
    else:
        return render_template('auth/login.html', auth=user)


@auth.route('/logout', strict_slashes=False)
def logout():
    user = True if 'username' in session else False
    if not user:
        flash('You are not logged in')
        return redirect(request.url)
    session.pop('username')
    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('username', '', expires=-1)

    return response
