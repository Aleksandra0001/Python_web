from Homework_10.api import generate_fake_contacts, add_phone, add_email, get_contact_by_id, add_contact, delete_contact
from styles import *
import timeit
# import redis
# import timeit
# from redis_lru import RedisLRU
#
# client = redis.StrictRedis(host="localhost", port=6379, password=None)
# print(client.info())
#
# cache = RedisLRU(client)


def menu():
    while True:
        pretty_title('Menu')
        option('1. Add contact')
        option('2. Add phone')
        option('3. Add email')
        option('4. Get contact by id')
        option('5. Delete contact')
        option('6. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            first_name = input('Enter first name: ').strip()
            last_name = input('Enter last name: ').strip()
            if not first_name or not last_name:
                warning('Please,enter first name and last name!')
                first_name = input('Enter first name: ').strip()
                last_name = input('Enter last name: ').strip()
            phone = input('Enter phone: ').strip()
            email = input('Enter email: ').strip()
            add_contact(first_name, last_name, phone, email)
        elif choice == '2':
            contact_id = input('Enter contact id: ').strip()
            phone = input('Enter phone: ').strip()
            add_phone(contact_id, phone)
        elif choice == '3':
            contact_id = input('Enter contact id: ').strip()
            email = input('Enter email: ').strip()
            add_email(contact_id, email)
        elif choice == '4':
            contact_id = input('Enter contact id: ').strip()
            start_time = timeit.default_timer()
            get_contact_by_id(contact_id)
            end_time = timeit.default_timer() - start_time
            print(f'Elapsed time: {end_time}')
        elif choice == '5':
            contact_id = input('Enter contact id: ').strip()
            delete_contact(contact_id)
        elif choice == '6':
            break
        else:
            warning('Wrong choice! Try again')


def main():
    pretty_title('Welcome to the contact book!')
    fake_data = input('Do you want to generate fake contacts? (y/n): ')
    if fake_data == 'y':
        generate_fake_contacts()
        message('Fake contacts generated successfully!')
        menu()
    else:
        message('Ok, no fake data!')
        menu()
