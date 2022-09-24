from flask import render_template, Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/')
def base():
    return render_template('base.html')


@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')


@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')
