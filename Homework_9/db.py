from sqlalchemy.orm import sessionmaker, declarative_base
import pathlib
from sqlalchemy import create_engine
import configparser


file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

url = f'postgresql://{username}:{password}@{domain}:5432/{db_name}'

Base = declarative_base()
engine = create_engine(url, echo=True, pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()