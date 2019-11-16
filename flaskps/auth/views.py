from flask import render_template, redirect, request
from flask_login import login_required, login_manager, login_user

from flaskps.users.models import User
from flaskps.auth.forms import LogInForm

from . import auth


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    """
    Muestra el template de login
    """
    import ipdb;ipdb.set_trace()
    form = LogInForm(request.form)

    if request.method == 'POST' and form.validate():

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user.verify_password(password):
            login_user(user)
            return redirect('/dashboard')
    return render_template('auth/login.html', title="login")


def logout():
    """
    Deslogea usuario de la session
    """
    pass


#@perm.current_user_loader
#def load_current_user():
#    if 'user_id' in session:
#        return User.query.get(session['user_id'])
