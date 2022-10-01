import os
from flask import Flask, redirect, url_for
from personal_app.routes import auth, contacts
from config import config
from flask_migrate import Migrate


migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.Config)
    from personal_app.models import db
    db.init_app(app)
    migrate.init_app(app, db)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.auth)
    app.register_blueprint(contacts.contact)
    app.add_url_rule('/', endpoint='index')

    @app.route('/')
    def index():
        return redirect(url_for('contacts.contacts'))

    return app

# export FLASK_APP=personal_app
# export FLASK_ENV=development
# runs on https://werkzeug.palletsprojects.com/en/2.0.x/
# flask run
