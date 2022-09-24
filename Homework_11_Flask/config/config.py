import pathlib

SECRET_KEY = b'g\xc0\x7f\x02[U\x9dJ\x10B\xae\x1cGK\x1b\xcb'
DB_NAME = 'contacts_db'
DEBUG = False

BASE_DIR = pathlib.Path(__file__).parent.parent
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'app.db.sqlite3')