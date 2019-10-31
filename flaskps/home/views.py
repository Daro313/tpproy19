from flask import render_template
from flask_login import login_required
from flaskps.models import Configurations

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    conf = Configurations.query.first()
    return render_template('home/index.html', conf=conf)


@home.route('/dashboard')
#@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")
