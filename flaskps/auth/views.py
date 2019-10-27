from flask import render_template
from flask_login import login_required

from . import auth


@auth.route('/login')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('auth/login.html', title="login")


@auth.route('/create_user')
# @login_required descomentar despues de crear el primer usuario
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('auth/create_user.html', title="creacion de usuario")
