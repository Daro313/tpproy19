from flask import render_template, redirect, request
from flask_login import login_required

from flaskps import db
from flaskps.models import User

from . import users

def update_user_template():
    pass

@users.route('user/create_form')
# @login_required descomentar despues de crear el primer usuario
def user_create_form():
    """
    Muestra el template de creacion de usuario
    """
    return render_template('user/create_user.html')


@users.route('user/create', methods=['POST'])
def create():
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
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return render_template('user/create_user.html'), 403

    return render_template('user/create_user.html'), 201, {'msg': 'el usuario se creo con exito'}


@users.route('/user/update/<user_id>', methods=['POST'])
def update(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    # TODO: crear form para validad
    name = request.form.get("first_name")
    surname = request.form.get("last_name")
    email = request.form.get("email")
    username = request.form.get("username")
    active = request.form.get("active")
    rol = request.form.get("rol")

    user.first_name = name
    user.last_name = surname
    if active is None:
        user.active = False
    else:
        user.active = True
    user.username = username
    user.rol = rol
    user.email = email

    db.session.commit()

    return redirect('/user/list')


@users.route('/user/list', methods=['GET'])
def list():
    users = User.query.all()
    return render_template('users/list.html', user_list=users)


@users.route('/user/detail/<username>')
def detail(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/detail.html', user=user)


def delete_user():
    pass


def activate_user():
    pass


def deactivate_user():
    pass
