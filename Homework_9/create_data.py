from faker import Faker
from sqlalchemy import exists, and_
from db import session, engine
from sqlalchemy.sql.expression import func
from models import (
    Contact, Phone, Email,
)

fake = Faker('uk_UA')


def generate_fake_contacts():
    for i in range(100):
        contact_first_name = fake.first_name()
        contact_last_name = fake.last_name()
        contact_phone = fake.phone_number()
        contact_email = fake.email()

        contact = Contact(
            first_name=contact_first_name,
            last_name=contact_last_name,
        )
        phone = Phone(
            phone=contact_phone,
            contact=contact,
        )
        email = Email(
            email=contact_email,
            contact=contact,
        )
        session.add(contact)
        session.add(phone)
        session.add(email)
        session.commit()


def add_phone(contact_id, phone):
    contact = session.query(Contact).filter(Contact.contact_id == contact_id).first()
    phone = Phone(
        phone=phone,
        contact=contact,
    )
    session.add(phone)
    session.commit()


def add_email(contact_id, email):
    contact = session.query(Contact).filter(Contact.contact_id == contact_id).first()
    email = Email(
        email=email,
        contact=contact,
    )
    session.add(email)
    session.commit()


def add_contact(first_name, last_name, phone, email):
    contact = Contact(
        first_name=first_name,
        last_name=last_name,
    )
    phone = Phone(
        phone=phone,
        contact=contact,
    )
    email = Email(
        email=email,
        contact=contact,
    )
    session.add(contact)
    session.add(phone)
    session.add(email)
    session.commit()


def get_contact_by_id(contact_id):
    contact = session.query(Contact).filter(Contact.contact_id == contact_id).first()
    return contact


def delete_contact(contact_id):
    contact = session.query(Contact).filter(Contact.contact_id == contact_id).first()
    session.delete(contact)
    session.commit()


