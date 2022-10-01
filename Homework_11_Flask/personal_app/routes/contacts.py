from flask import Flask, render_template, Blueprint, request, session, redirect, url_for, flash
from personal_app.repository.contacts import create_contact, get_user_contacts, delete_contact

contact = Blueprint('contacts', __name__, url_prefix='/contacts')


@contact.route('/', methods=['GET', 'POST'], strict_slashes=False)
def contacts():
    user = True if 'username' in session else False
    if not user:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        new_contact = create_contact(name, surname, email, phone, user_id=session['username']['id'])
        flash(f'Contact {new_contact.first_name} {new_contact.last_name} was created')
        user_contacts = get_user_contacts(session['username']['id'])
        return render_template('contacts/contacts.html', contacts=user_contacts)
    user_contacts = get_user_contacts(session['username']['id'])
    return render_template('contacts/contacts.html', contacts=user_contacts, auth=user)


@contact.route('/delete/<contact_id>', methods=['POST'], strict_slashes=False)
def delete(contact_id):
    user = True if 'username' in session else False
    if not user:
        return redirect(request.url)
    if request.method == 'POST':
        delete_contact(contact_id, session['username']['id'])
        flash('Operation successfully!')
    return redirect(url_for('contacts.contacts'))
