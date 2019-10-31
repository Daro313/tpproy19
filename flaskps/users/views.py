from flask import render_template, redirect, request
from flask_login import login_required

from flaskps import db
from flaskps.models import User

from . import users

def update_user_template():
    pass


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

@users.route('/user/delete/<user_id>', methods=['POST'])
def delete(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect('/user/list')
def activate_user():
    pass

def deactivate_user():
    pass
