from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
_CONNECTION = 'sqlite:///address_book.db'

engine = create_engine(_CONNECTION, echo=True)
metadata = Base.metadata
DBSession = sessionmaker(bind=engine)
session = DBSession()