from sqlalchemy import and_

from personal_app.models import db, Contact, Phone


def create_contact(name, surname, email, phone, user_id):
    contact = Contact(first_name=name, last_name=surname, email=email, user_id=user_id)
    contact.phones.append(Phone(phone=phone))
    db.session.add(contact)
    db.session.commit()
    return contact


def get_contact_by_id(contact_id):
    return Contact.query.get(contact_id)


def get_user_contacts(user_id):
    return Contact.query.filter_by(user_id=user_id).all()


def get_user_contacts_with_phones(user_id):
    contacts = db.session.query(Contact, Phone).filter(
        and_(Contact.user_id == user_id, Contact.contact_id == Phone.contact_id)).all()
    return contacts


def get_user_contact(contact_id, user_id):
    return db.session.query(Contact).filter(
        and_(Contact.user_id == user_id, Contact.contact_id == contact_id)).one()


def delete_contact(contact_id, user_id):
    db.session.query(Contact).filter(
        and_(Contact.user_id == user_id, Contact.contact_id == contact_id)).delete()
    db.session.commit()


def update_contact(contact_id, user_id, name, surname, email, phone):
    contact = get_user_contact(contact_id, user_id)
    contact.first_name = name
    contact.last_name = surname
    contact.email = email
    contact.phones[0].phone = phone
    db.session.commit()
    return contact
