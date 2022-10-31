from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///news.db'
print('DB_URL', DB_URL)

engine = create_engine(DB_URL, echo=True)
