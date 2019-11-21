import jinja2
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

login_manager = LoginManager()
db = SQLAlchemy()

BASE_DIR = os.getcwd()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "Logeo necesario."
    login_manager.login_view = "auth.login"
    # setup templates config
    my_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader([
                '%s/flaskps/app/auth/templates/' % BASE_DIR,
                '%s/flaskps/app/configurations/templates/' % BASE_DIR,
                '%s/flaskps/app/students/templates/' % BASE_DIR,
                '%s/flaskps/app/home/templates/' % BASE_DIR,
                '%s/flaskps/app/users/templates/' % BASE_DIR,
                '%s/flaskps/app/teachers/templates/' % BASE_DIR,
            ]),
        ])
    app.jinja_loader = my_loader
    migrate = Migrate(app, db)
    from flaskps import models
    from .app.students import students as students_blueprint
    app.register_blueprint(students_blueprint)
    from .app.configurations import configurations as configurations_blueprint
    app.register_blueprint(configurations_blueprint)
    from .app.teachers import teachers as teachers_blueprint
    app.register_blueprint(teachers_blueprint)
    from .app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from .app.users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    from .app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
