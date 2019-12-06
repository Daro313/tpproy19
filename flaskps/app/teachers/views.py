import requests
from flask_login import login_required
from flask_user import current_user

from flask import render_template, redirect, request, url_for

from flaskps import db
from . import teachers
from .models import Teachers
from .forms import CreateTeachersForm
from flaskps.app.configurations.models import Configurations


@teachers.route('/teachers/create', methods=['GET', 'POST'])
@login_required
def create(permiso='teachers_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateTeachersForm(request.form)
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()

        if request.method == 'POST' and form.validate():
            teacher = Teachers(
                name=request.form.get('name'),
                surname=request.form.get('surname'),
                birth_date=request.form.get('birth_date'),
                locality=request.form.get('locality'),
                address=request.form.get('address'),
                document_type=request.form.get('document_type'),
                document_number=request.form.get('document_number'),
                phone=request.form.get('phone'),
            )
            db.session.add(teacher)
            try:
                db.session.commit()
                msg = "El Docente %s se creo con exito" % teacher.name
            except:
                db.session.rollback()
                return render_template('teachers/create.html', form=form, dniTypes=dniTypes, localities=localities), 403
            return redirect(url_for('teachers.detail', teacher_id=teacher.id))
        return render_template('teachers/create.html', form=form, dniTypes=dniTypes, localities=localities)
    else:
        return render_template('home/dashboard.html')


@teachers.route('/teachers/list/', methods=['GET'], defaults={'page':1})
@teachers.route('/teachers/list/<int:page>', methods=['GET'])
@login_required
def list(page,permiso='teachers_index'):
    if current_user.have_permissions(permiso):
        page = page
        conf = Configurations.query.first()
        teachers = Teachers.query.filter_by()
        teachers = teachers.paginate(page, conf.offset_paginator, False)
        return render_template('teachers/list.html', teachers=teachers)
    else:
        return render_template('home/dashboard.html')


@teachers.route('/teachers/detail/<int:teacher_id>', methods=['GET','POST'])
@login_required
def detail(teacher_id,permiso='teachers_show'):
    if current_user.have_permissions(permiso):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        return render_template('teachers/detail.html', teacher=teacher)
    else:
        return render_template('home/dashboard.html')


@teachers.route('/teachers/delete/<int:teacher_id>', methods=['POST'])
@login_required
def delete(teacher_id,permiso='teachers_destroy'):
    if current_user.have_permissions(permiso):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        db.session.delete(teacher)
        db.session.commit()
        return redirect(url_for('teachers.list'))
    else:
        return render_template('home/dashboard.html')


@teachers.route('/teachers/update/<int:teacher_id>', methods=['GET', 'POST'])
@login_required
def update(teacher_id,permiso='teachers_update'):
    if current_user.have_permissions(permiso):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()

        if request.method == "POST":
            form = CreateTeachersForm(request.form)
            if form.validate():
                teacher.update(form)
                return redirect(url_for('teachers.detail', teacher_id=teacher.id))
        return render_template('teachers/edit.html', teacher=teacher, dniTypes=dniTypes, localities=localities), 200
    else:
        return render_template('home/dashboard.html')
