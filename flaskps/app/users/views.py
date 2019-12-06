from flask import render_template, redirect, request, url_for
from flask_login import login_required
from flask_user import current_user, roles_required, UserManager

from flaskps.utils.functions import get_user_roles
from flaskps import db
from flaskps.app.users.models import User, Rol, UserRoles
from flaskps.app.configurations.models import Configurations
from flaskps.app.users.forms import CreateFormUser

from . import users


@users.route('/user/create', methods=['GET', 'POST'])
@login_required
def create(permiso='user_new'):
    """
    Si los datos son validos crea un nuevo usuario
    """
    if current_user.have_permissions(permiso):
        form = CreateFormUser(request.form)
        if request.method == 'POST' and form.validate():
            user = User(
                name=request.form.get('name'),
                surname=request.form.get('surname'),
                email=request.form.get('email'),
                username=request.form.get('username'),
            )
            user.password = request.form.get('password')
            roles = request.form.getlist('roles')

            roles = Rol.query.filter(Rol.name.in_(roles)).all()
            user.roles = roles
            db.session.add(user)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                return render_template('users/create_user.html', msg= 'No se pudo crear el usuario'), 403
            return redirect(url_for('users.detail', user_id=user.id))
        return render_template('users/create_user.html', form=form)
    else:
        return render_template('home/dashboard.html')


@users.route('/user/list/', methods=['GET', 'POST'], defaults={'page':1})
@users.route('/user/list/<int:page>', methods=['GET', 'POST'])
@login_required
def list(page,permiso='user_index'):
    if current_user.have_permissions(permiso):
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
    else:
        return render_template('home/dashboard.html')


@users.route('/user/update/int:<user_id>', methods=['GET','POST'])
@login_required
def update(user_id,permiso='user_update'):
    if current_user.have_permissions(permiso):
        user = User.query.filter_by(id=user_id).first_or_404()
        roles = get_user_roles(user)
        if request.method == "POST":
            form = CreateFormUser(request.form)
            if form.validate():
                user.update(form)
                return redirect(url_for('users.detail', user_id=user.id))
        return render_template('users/edit.html', user=user, roles=roles), 200
    else:
        return render_template('home/dashboard.html')


@users.route('/user/detail/<int:user_id>')
@login_required
def detail(user_id,permiso='user_show'):
    if current_user.have_permissions(permiso):
        user = User.query.filter_by(id=user_id).first_or_404()
        return render_template('users/detail.html', user=user)
    else:
        return render_template('home/dashboard.html')


@users.route('/user/delete/<user_id>', methods=['POST'])
@login_required
def delete(user_id,permiso='user_destroy'):
    if current_user.have_permissions(permiso):
        user = User.query.filter_by(id=user_id).first_or_404()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.list'))
    else:
        return render_template('home/dashboard.html')
