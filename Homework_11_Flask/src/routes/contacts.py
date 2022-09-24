from flask import Flask, render_template, Blueprint

contacts_bp = Blueprint('contacts', __name__, url_prefix='/contacts')


@contacts_bp.route('/contacts')
def contacts():
    return 'This is the contacts page'


@contacts_bp.route('/contacts/create')
def create():
    return 'Create a new todo'
