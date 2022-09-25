from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.String(255), nullable=False)

    token_cookie = db.Column(db.String(255), nullable=True, default=None)
    contacts = relationship('Contact', back_populates='user')

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"


class Contact(db.Model):
    __tablename__ = 'contacts'
    contact_id = db.Column('contact_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(50), nullable=False)
    last_name = db.Column('last_name', db.String(50), nullable=False)
    email = db.Column('email', db.String(50), nullable=True, default='No email')
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    phones = relationship("Phone", back_populates="contact", cascade="all, delete-orphan")
    user = relationship('User', cascade='all, delete', back_populates='contacts')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f"Contact({self.id}, {self.first_name},{self.last_name})"


class Phone(db.Model):
    __tablename__ = 'phones'
    phone_id = db.Column('phone_id', db.Integer, primary_key=True)
    phone = db.Column('phone', db.String(50), nullable=True, default='No phone')
    contact_id = db.Column('contact_id', db.Integer, ForeignKey('contacts.contact_id'), nullable=False)
    contact = relationship("Contact", back_populates="phones")

    def __repr__(self):
        return f"Phone({self.id}, {self.phone})"


