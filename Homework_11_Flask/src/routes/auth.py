from flask import render_template

from src import app


@app.route('/hi')
def index():
    return 'Im alive!'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/register')
def register():
    return render_template('auth/register.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')
