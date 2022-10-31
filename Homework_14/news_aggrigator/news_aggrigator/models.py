from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

news_to_author = Table(
    "news_to_author",
    Base.metadata,
    Column("news_id", Integer, ForeignKey("news.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.id"), primary_key=True),
)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_url = Column(String(250), nullable=True)
    title = Column(String(150), nullable=False, unique=True)
    content = Column(String(2000), nullable=False)
    date = Column(String(50))
    created_at = Column(DateTime, default=datetime.now())
    author = relationship("Author", secondary=news_to_author, back_populates="news")
    # author = relationship("Author", secondary=news_to_author, backref="author")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    news = relationship("News", secondary=news_to_author, back_populates="author")
