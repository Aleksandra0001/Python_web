from bson import ObjectId
from faker import Faker

from Homework_10.lru_cache import redis_cache
from models import Contact
from random import randint
from styles import *

# import redis
# from functools import lru_cache

# client = redis.StrictRedis(host="localhost", port=6379, password=None)
# print(client.info())

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


@redis_cache
def get_contact_by_id(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    return print(contact.first_name, contact.last_name, contact.phone, contact.email)


def delete_contact(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.delete()
    message('Contact deleted successfully!')
