from flask import render_template
from flask import request
from flask_login import login_required

from models import User

from . import auth


@auth.route('/login')
def login():
    """
    Muestra el template de login
    """
    return render_template('auth/login.html', title="login")


@auth.route('/user_create_form')
# @login_required descomentar despues de crear el primer usuario
def user_create_form():
    """
    Muestra el template de creacion de usuario
    """
    return render_template('auth/create_user.html', title="creacion de usuario")


@auth.route('/create_user', methods=['POST'])
def create_user():
    """
    Si los datos son validos crea un nuevo usuario
    """
    print('sdfasdfas')
    data = requst.data
    User.query.create(**data)

def create(self, *args, **kwargs)
    
    User.query.create(
        email=data['email'],
        username=data['username']
    )

    import ipdb;ipdb.set_trace()
    return render_template('user/list.html', tittle='lista de usuarios')
