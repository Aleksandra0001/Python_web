from flask import Flask, render_template, Blueprint

contact = Blueprint('contacts', __name__, url_prefix='/contacts')


@contact.route('/contacts')
def contacts():
    return 'This is the contacts page'


@contact.route('/contacts/create')
def create():
    return 'Create a new todo'
