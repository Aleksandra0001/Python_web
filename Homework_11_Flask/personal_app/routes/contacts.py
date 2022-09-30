from flask import Flask, render_template, Blueprint, request
from personal_app.repository.contacts import create_contact, get_user_contacts

contact = Blueprint('contacts', __name__, url_prefix='/contacts')


@contact.route('/', methods=['GET', 'POST'], strict_slashes=False)
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        new_contact = create_contact(name, surname, email, phone, user_id=5)
        user_contacts = get_user_contacts(user_id=5)
        return render_template('contacts/contacts.html', contacts=user_contacts)

    return render_template('contacts/contacts.html')
