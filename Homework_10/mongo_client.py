import configparser
import pathlib
from mongoengine import connect

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)
print(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'pass')
db = config.get('DB', 'db')

mongo_client = connect(
    db=db,
    username=username,
    password=password,
    host=f'mongodb+srv://{username}:{password}@cluster0.qh8el1i.mongodb.net/{db}?retryWrites=true&w=majority'
)
