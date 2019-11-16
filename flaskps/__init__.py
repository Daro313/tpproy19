from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Logeo necesario."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from flaskps import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    from .configurations import configurations as configurations_blueprint
    app.register_blueprint(configurations_blueprint)

    return app
