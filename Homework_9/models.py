from sqlalchemy import (
    ForeignKey,
    Column,
    Integer, String, Date,
    DateTime,
    Table,Identity
)
from sqlalchemy.orm import relationship

from db import Base, metadata


class Contact(Base):
    __tablename__ = 'contacts'
    contact_id = Column('contact_id', Integer, primary_key=True)
    first_name = Column('first_name', String(50), nullable=False)
    last_name = Column('last_name', String(50), nullable=False)
    phone = relationship("Phone", back_populates="contact", cascade="all, delete-orphan")
    email = relationship("Email", back_populates="contact", cascade="all, delete-orphan")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Phone(Base):
    __tablename__ = 'phones'
    phone_id = Column('phone_id', Integer, primary_key=True)
    phone = Column('phone', String(50), nullable=True,default='No phone')
    contact_id = Column('contact_id', Integer, ForeignKey('contacts.contact_id'), nullable=False)
    contact = relationship("Contact", back_populates="phone")


class Email(Base):
    __tablename__ = 'emails'
    email_id = Column('email_id', Integer, primary_key=True)
    email = Column('email', String(50), nullable=True,default='No email')
    contact_id = Column('contact_id', Integer, ForeignKey('contacts.contact_id'), nullable=False)
    contact = relationship("Contact", back_populates="email")
