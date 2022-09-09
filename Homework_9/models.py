from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import DateTime

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(50), nullable=False)
    phone = Column('phone_number', String(50), nullable=False)
    birthday = Column('birthday', DateTime, nullable=False)
    address = Column('address', String(50), nullable=False)


class Notebook_record(Base):
    __tablename__ = "notebook_record"
    id = Column('id', Integer, primary_key=True)
    notebook_title = Column('notebook_title', String(50), nullable=False)
    notebook_text = Column('notebook_text', String(500), nullable=False)
    notebook_tag = Column('notebook_tag', String(50), nullable=False)
