from faker import Faker
from models import Contact


fake = Faker('uk_UA')


def generate_fake_contacts():
    for i in range(30):
        contact_first_name = fake.first_name()
        contact_last_name = fake.last_name()
        contact_phone = fake.phone_number()
        contact_email = fake.email()
        new_fake_contact = Contact(first_name=contact_first_name, last_name=contact_last_name, phone=[contact_phone], email=contact_email)
        new_fake_contact.save()


def add_phone(contact_id, phone):
    pass


def add_email(contact_id, email):
    pass


def add_contact(first_name, last_name, phone, email):
    pass


def get_contact_by_id(contact_id):
    pass


def delete_contact(contact_id):
    pass
