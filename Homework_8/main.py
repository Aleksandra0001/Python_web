from random import randint, choice

import psycopg2
from contextlib import contextmanager
from sqlite3 import Error
from faker import Faker

fake = Faker()


@contextmanager
def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='university', user='postgres', password='password')
        print('Connected!')
        yield conn
        conn.commit()
    except Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def create_table():
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS class (
                            id SERIAL PRIMARY KEY,
                            class_name VARCHAR(30) NOT NULL)''')

            cur.execute('''CREATE TABLE IF NOT EXISTS student (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(30) NOT NULL,
                            class_id INTEGER REFERENCES class(id))''')

            cur.execute('''CREATE TABLE IF NOT EXISTS mentor (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(30) NOT NULL)''')

            cur.execute('''CREATE TABLE IF NOT EXISTS subject (
                            id SERIAL PRIMARY KEY,
                            subject_name VARCHAR(30) NOT NULL,
                            mentor_id INTEGER REFERENCES mentor(id))''')

            cur.execute('''CREATE TABLE IF NOT EXISTS mark (
                            id SERIAL PRIMARY KEY,
                            mark INTEGER NOT NULL,
                            data_of_mark date NOT NULL,
                            student_id INTEGER REFERENCES student(id),
                            subject_id INTEGER REFERENCES subject(id))''')
        conn.commit()


def insert_data():
    with create_connection() as conn:
        with conn.cursor() as cursor:
            for i in range(3):
                cursor.execute(
                    "INSERT INTO class (class_name) VALUES (%s)", (fake.bothify(text='Class: ??-##', letters='ABCDE'),))

            cursor.execute("SELECT id FROM class")
            class_ids = cursor.fetchall()
            conn.commit()

            for i in range(30):
                cursor.execute(
                    "INSERT INTO student (name, class_id) VALUES (%s, %s)",
                    (fake.name(), choice(class_ids),))

            for i in range(3):
                cursor.execute(
                    "INSERT INTO mentor (name) VALUES (%s)", (fake.name(),))

            cursor.execute("SELECT id FROM mentor")
            mentor_ids = cursor.fetchall()
            conn.commit()

            for subject in ['Math', 'Physics', 'Chemistry', 'Biology', 'History']:
                cursor.execute(
                    "INSERT INTO subject (subject_name, mentor_id) VALUES (%s, %s)",
                    (subject, choice(mentor_ids),))

            cursor.execute("SELECT id FROM subject")
            subject_ids = cursor.fetchall()
            conn.commit()

            cursor.execute("SELECT id FROM student")
            student_ids = cursor.fetchall()
            conn.commit()

            for student in student_ids:
                for subject in subject_ids:
                    for i in range(20):
                        cursor.execute(
                            "INSERT INTO mark (mark, data_of_mark, student_id, subject_id) VALUES (%s, %s, %s, %s)",
                            (randint(1, 12), fake.date_this_year(), student[0], subject[0],))


if __name__ == '__main__':
    # create_table()
    # insert_data()
    print('Table created!')
