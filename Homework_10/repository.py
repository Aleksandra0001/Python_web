from bson import ObjectId
from faker import Faker
from mongoengine import DoesNotExist

from lru_cache import cache, LruCache
from models import Contact
from random import randint
from styles import *

fake = Faker('uk_UA')


def generate_fake_contacts():
    for i in range(30):
        fake_contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=[fake.phone_number() for i in range(randint(1, 3))],
            email=fake.email())
        fake_contact.save()


def add_contact(first_name, last_name, phone, email):
    new_contact = Contact(first_name=first_name, last_name=last_name, phone=[phone], email=email)
    new_contact.save()


def add_phone(contact_id, phone):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.phone.append(phone)
    contact.save()
    message('Phone added successfully!')


def add_email(contact_id, email):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact_email = contact.email
    if contact_email == email:
        warning('This email already exists!')
    else:
        contact.email = email
        contact.save()
        message('Email added successfully!')


@LruCache
def get_contact_by_id(contact_id):
    try:
        contact = Contact.objects.get(id=ObjectId(contact_id))
        contact_cache_value = {
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'email': contact.email,
            'phone': contact.phone
        }
        return contact_cache_value
    except DoesNotExist:
        warning('Contact does not exist!')



def delete_contact(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.delete()
    message('Contact deleted successfully!')
