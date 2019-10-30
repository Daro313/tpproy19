from flask import render_template
from flask import request
from flask_login import login_required

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Muestra el template de login
    """
    if request.method == 'POST':
        return "do_the_login()"
    else:
        return render_template('auth/login.html', title="login")


def logout():
    """
    Deslogea usuario de la session
    """
    pass
