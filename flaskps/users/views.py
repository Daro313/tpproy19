from flask import render_template, redirect, request, url_for
from flask_login import login_required

from flaskps import db
from flaskps.users.models import User
from flaskps.configurations.models import Configurations
from flaskps.users.forms import CreateFormUser

from . import users


@users.route('/user/create', methods=['GET', 'POST'])
@login_required
def create():
    """
    Si los datos son validos crea un nuevo usuario
    """
    form = CreateFormUser(request.form)

    if request.method == 'POST' and form.validate():
        name = request.form.get('first_name')
        surname = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('user_name')
        rol = request.form.get('roles')

        user = User(
            name=name,
            surname=surname,
            email=email,
            username=username,
        )
        user.password = password
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return render_template('users/create_user.html', msg= 'No se pudo crear el usuario'), 403
        return render_template('users/create_user.html', msg='Usuario {} creado con exito'.format(name)), 201
    return render_template('users/create_user.html', form=form)



@users.route('/user/update/<user_id>', methods=['POST'])
@login_required
def update(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()

    # TODO: crear form para validad
    name = request.form.get("first_name")
    surname = request.form.get("last_name")
    email = request.form.get("email")
    username = request.form.get("username")
    active = request.form.get("active")
    rol = request.form.get("rol")

    user.name = name
    user.surname = surname
    if active is None:
        user.active = False
    else:
        user.active = True
    user.username = username
    user.rol = rol
    user.email = email

    db.session.commit()

    return redirect(url_for('users.list'))


@users.route('/user/list/', methods=['GET', 'POST'], defaults={'page':1})
@users.route('/user/list/<int:page>', methods=['GET', 'POST'])
@login_required
def list(page):
    page=page
    users = User.query.filter_by()
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        active = form.get('active')
        if username:
            users = users.filter_by(username=username)
        if active:
            active = True if active == "True" else False
            users = users.filter_by(active=active)

    conf = Configurations.query.first()

    users = users.paginate(page, conf.offset_paginator, False)

    return render_template('users/list.html', user_list=users)


@users.route('/user/detail/<username>')
@login_required
def detail(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/detail.html', user=user)


@users.route('/user/delete/<user_id>', methods=['POST'])
@login_required
def delete(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.list'))

@login_required
def activate_user():
    pass


@login_required
def deactivate_user():
    pass
