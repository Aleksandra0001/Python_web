from sqlalchemy import and_

from personal_app.models import db, Contact, Phone


def create_contact(name, surname, email, phone, user_id):
    contact = Contact(first_name=name, last_name=surname, email=email, user_id=user_id)
    contact.phones.append(Phone(phone=phone))
    db.session.add(contact)
    db.session.commit()
    return contact


def get_user_contacts(user_id):
    return Contact.query.filter_by(user_id=user_id).all()


def get_user_contact(contact_id, user_id):
    return db.session.query(Contact).filter(
        and_(Contact.user_id == user_id, Contact.id == contact_id)).one()


def delete_contact(contact_id, user_id):
    contact = Contact.query.filter_by(id=contact_id, user_id=user_id).first()
    db.session.delete(contact)
    db.session.commit()
