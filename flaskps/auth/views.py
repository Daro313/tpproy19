from flask import render_template
from flask import request
from flask_login import login_required

from . import auth


@auth.route('/login')
def login():
    """
    Muestra el template de login
    """
    return render_template('auth/login.html', title="login")


def logout():
    """
    Deslogea usuario de la session
    """
    pass
