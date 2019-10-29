from flask import render_template
from flask import request
from flask_login import login_required

from flaskps import db
from flaskps.models import User

from . import admin


@admin.route('/user_create_form')
# @login_required descomentar despues de crear el primer usuario
def user_create_form():
    """
    Muestra el template de creacion de usuario
    """
    return render_template('admin/create_user.html', title="creacion de usuario")


@admin.route('/create_user', methods=['POST'])
def create_user():
    """
    Si los datos son validos crea un nuevo usuario
    """
    data_dict = {}
    data = request.data.decode()
    data = data.replace("{", "").replace("}", "").replace('\"', "")
    data = data.split(',')

    for d in data:
        d = d.split(':')
        data_dict.update({d[0]: d[1]})

    name = data_dict.get('name')
    surname = data_dict.get('surname')
    email = data_dict.get('email')
    password = data_dict.get('password')
    username = data_dict.get('username')
    rol = data_dict.get('rol')

    user = User(
        first_name=name,
        last_name=surname,
        email=email,
        username=username,
        rol=rol
    )
    user.password = password
    db.session.add(user)
    db.session.commit()

    return render_template(
        'admin/create_user.html', title="se creo el usario con exito")
