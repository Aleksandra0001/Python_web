from random import randint

import psycopg2
from contextlib import contextmanager
from sqlite3 import Error
from faker import Faker

fake = Faker()


@contextmanager
def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='2902')
        print(conn)
        yield conn
        conn.commit()
    except Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
     id serial PRIMARY KEY,
     name VARCHAR(30)
    );"""
    sql_create_group_table = """CREATE TABLE IF NOT EXISTS "group" (
        id SERIAL PRIMARY KEY,
        "group"(name) VARCHAR(60),
        students INTEGER REFERENCES users(id)
    );"""
    sql_create_courses_table = """CREATE TABLE IF NOT EXISTS course (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(150),
        group INTEGER REFERENCES users(id)
    );"""
    sql_create_mentor_table = """CREATE TABLE IF NOT EXISTS mentor (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL
        course INTEGER REFERENCES courses(id)
        );"""
    sql_create_mark_table = """CREATE TABLE IF NOT EXISTS mark (
    id SERIAL PRIMARY KEY,
    mark numeric CHECK (mark > 1 AND mark < 5),
    data_of_mark date,
    student INTEGER REFERENCES users(id),
    course INTEGER REFERENCES courses(id),
    mentor INTEGER REFERENCES students_courses(id)
    );"""
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_students_table)
        else:
            print('Error: can\'t create the database connection')

    sql_insert_students_table = "INSERT INTO students(name) VALUES(%s)"
    sql_insert_group_table = "INSERT INTO group(name) VALUES(%s)"
    sql_insert_courses_table = "INSERT INTO course(course_name, group(name)) VALUES(%s, %s)"
    sql_insert_mentor_table = "INSERT INTO mentor(name, course) VALUES(%s, %s)"
    sql_insert_mark_table = "INSERT INTO mark(mark, data_of_mark, student, course, mentor) VALUES(%s, %s, %s, %s, %s) "

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            for _ in range(30):
                pass
                # ========var1======
                # cur.execute(sql_insert_students_table, (fake.name()), sql_insert_group_table,
                #             (fake.group()), sql_insert_courses_table, (fake.course_name(), fake.group()),
                #             sql_insert_mentor_table, (fake.name(), fake.course_name()),
                #             sql_insert_mark_table, (randint(1, 5), fake.date(), fake.name(), fake.course_name(), fake.name()))
            # ========var2======
                # cur.execute(sql_insert_students_table, (fake.name()))
                # cur.execute(sql_insert_group_table, (fake.group()))
                # cur.execute(sql_insert_courses_table, (fake.course_name(), fake.group()))
                # cur.execute(sql_insert_mentor_table, (fake.name(), fake.course_name()))
                # cur.execute(sql_insert_mark_table, (randint(1, 5), fake.date(), fake.name(), fake.course_name(), fake.name()))
            cur.close()
        else:
            print('Error: can\'t create the database connection')
