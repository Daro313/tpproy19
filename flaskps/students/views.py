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
        student = Student(
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
            msg = "El Estudiante %s" % student.name
        except:
            db.session.rollback()

            return render_template('students/create.html', form=form.erros), 403
        return render_template('students/create.html', msg=msg), 201

    return render_template('students/create.html', form=form)


