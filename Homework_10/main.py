import configparser
import pathlib
from mongoengine import connect
from view import main

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)
print(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'pass')
db = config.get('DB', 'db')

connect(
    db=db,
    username=username,
    password=password,
    host=f'mongodb+srv://{username}:{password}@cluster0.qh8el1i.mongodb.net/{db}?retryWrites=true&w=majority'
)

if __name__ == '__main__':
    main()
