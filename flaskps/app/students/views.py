import requests
from flask_login import login_required
from flask import render_template, redirect, request, url_for, flash
from flask_user import current_user

from flaskps import db
from . import students
from .models import Students
from .forms import CreateStudentsForm
from flaskps.app.configurations.models import Configurations


@students.route('/students/create', methods=['GET', 'POST'])
@login_required
def create(permiso='students_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateStudentsForm(request.form)
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()
        if request.method == 'POST' and form.validate():
            student = Students(
                name=request.form.get('name'),
                surname=request.form.get('surname'),
                birth_date=request.form.get('birth_date'),
                borned=request.form.get('borned'),
                locality=request.form.get('locality'),
                address=request.form.get('address'),
                neighborhood=request.form.get('neighborhood'),
                gender=request.form.get('gender'),
                document_type=request.form.get('document_type'),
                document_number=request.form.get('document_number'),
                tutor=request.form.get('tutor'),
                phone=request.form.get('phone'),
                school=request.form.get('school'),
                level=request.form.get('level'),
            )
            db.session.add(student)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                return render_template('students/create.html', form=form, dniTypes=dniTypes, localities=localities), 403
            return redirect(url_for('students.detail', student_id=student.id))
        return render_template('students/create.html', form=form, dniTypes=dniTypes, localities=localities)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')

@students.route('/students/list/', methods=['GET'], defaults={'page':1})
@students.route('/students/list/<int:page>', methods=['GET'])
@login_required
def list(page,permiso='students_index'):
    if current_user.have_permissions(permiso):
        page = page
        conf = Configurations.query.first()
        students = Students.query.filter_by()
        students = students.paginate(page, conf.offset_paginator, False)
        return render_template('students/list.html', students=students)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@students.route('/students/detail/<int:student_id>', methods=['GET','POST'])
@login_required
def detail(student_id,permiso='students_show'):
    if current_user.have_permissions(permiso):
        student = Students.query.filter_by(id=student_id).first_or_404()
        return render_template('students/detail.html', student=student)
    else:
        return render_template('home/dashboard.html')

@students.route('/students/delete/<int:student_id>', methods=['POST'])
@login_required
def delete(student_id,permiso='students_destroy'):
    if current_user.have_permissions(permiso):
        student = Students.query.filter_by(id=student_id).first_or_404()
        db.session.delete(student)
        db.session.commit()
        return redirect('/students/list')
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@students.route('/students/update/<int:student_id>', methods=['GET', 'POST'])
@login_required
def update(student_id,permiso='students_update'):
    if current_user.have_permissions(permiso):
        student = Students.query.filter_by(id=student_id).first_or_404()
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()
        if request.method == "POST":
            form = CreateStudentsForm(request.form)
            if form.validate():
                student.update(form)
                return redirect(url_for('students.detail', student_id=student.id))
        return render_template('students/edit.html', student=student, localities=localities, dniTypes=dniTypes, form=form), 200
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')
