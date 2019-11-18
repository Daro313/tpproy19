from flask_login import login_required

from flask import render_template, redirect, request

from flaskps import db
from . import students
from .models import Students
from .forms import CreateStudentsForm


@students.route('/students/create', methods=['GET', 'POST'])
@login_required
def create():
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    form = CreateStudentsForm(request.form)

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
            msg = "El Estudiante %s se creo con exito" % student.name
        except:
            db.session.rollback()

            return render_template('students/create.html', form=form), 403
        return render_template('students/create.html', msg=msg, form=form), 201

    return render_template('students/create.html', form=form)

@students.route('/students/list/<int:page>', methods=['GET'])
@login_required
def list(page):
    import ipdb; ipdb.set_trace()
    page = page
    conf = Configurations.query.first()
    students = Students.query.filter_by()
    students = students.paginate(page, conf.offset_paginator, False)

    return render_template('students/list.html', students=students)
