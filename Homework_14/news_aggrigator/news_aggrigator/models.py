from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.schema import ForeignKey, Table
from .db import Base


many_to_many = Table(
    "many_to_many",
    Base.metadata,
    Column("news_id", Integer, ForeignKey("news.id")),
    Column("author_id", Integer, ForeignKey("author.id")),
)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_url = Column(String(250), nullable=True)
    title = Column(String(150), nullable=False, unique=True)
    content = Column(String(2000), nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    author = relationship("Author", secondary=many_to_many, backref="author")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
