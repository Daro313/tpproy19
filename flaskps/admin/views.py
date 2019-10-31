from flask import render_template
from flask import request
from flask_login import login_required

from flaskps import db
from flaskps.models import User

from . import admin








# @app.errorhandler(404)
#def page_not_found(e):
#    # note that we set the 404 status explicitly
#    return render_template('404.html'), 404
