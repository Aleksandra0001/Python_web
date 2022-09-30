from personal_app.models import db, Contact


def create_contact(name, surname, email, phone, user_id):
    contact = Contact(first_name=name, last_name=surname, email=email, user_id=user_id)
    db.session.add(contact)
    db.session.commit()
    return contact


def get_user_contacts(user_id):
    return Contact.query.filter_by(user_id=user_id).all()
