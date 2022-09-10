from faker import Faker
from sqlalchemy import exists, and_
from db import session, engine
from sqlalchemy.sql.expression import func
from models import (
    Contact, Phone, Email,
)

fake = Faker()


def create_contacts():
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
