import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent


class Config:
    SECRET_KEY = b'g\xc0\x7f\x02[U\x9dJ\x10B\xae\x1cGK\x1b\xcb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'app.db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
