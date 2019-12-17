from flask_login import login_required
from flask import render_template, redirect, request, url_for

from . import administration
from .models import SchoolYear, Workshop
from .forms import CreateSchoolYearForm, WorkshopCreateForm
from flaskps.app.configurations.models import Configurations
from flaskps.app.teachers.models import Teachers
from flaskps.app.students.constants import NEIGHBORHOOD_CHOICES


@administration.route('/school-year/create', methods=['GET', 'POST'])
@login_required
def school_year_create():
    """
    metodo GET: renderiza form de creacion
    metodo POST: verifica los datos y crea usuaraio
    """
    form = CreateSchoolYearForm(request.form)
    if request.method == 'POST' and form.validate():
        school_year = SchoolYear.create(form)
        return redirect(url_for('administration.school_year_detail', school_year_id=school_year.id))
    return render_template('administration/school_year_create.html')


@administration.route('/school-year/delete/<int:school_year_id>', methods=['POST'])
@login_required
def school_year_delete():
    pass

@administration.route('/school-year/detail/<int:school_year_id>', methods=['GET'])
@login_required
def school_year_detail(school_year_id):
    school_year = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
    return render_template('administration/school_year_detail.html', school_year=school_year)


@administration.route('/school-year/list', methods=['GET'], defaults={'page':1})
@administration.route('/school-year/list/<int:page>', methods=['GET'])
@login_required
def school_year_list(page):
    conf = Configurations.query.first()
    school_years = SchoolYear.query.filter_by().paginate(
                        page,
                        conf.offset_paginator,
                        False
                    )

    return render_template(
            'administration/school_year_list.html', school_years=school_years)


@administration.route('/workshop/craete/<int:school_year_id>', methods=['GET', 'POST'])
@login_required
def workshop_create(school_year_id):
    sy = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
    teachers = Teachers.query.all()
    form = WorkshopCreateForm(request.form)
    if request.method == "POST" and form.validate():
        import ipdb;ipdb.set_trace()
        workshop = Workshop.create(form, sy)
        return redirect(
                url_for('administration.workshop_detail', workshop_id=workshop.id))
    return render_template(
                'administration/workshop_create.html',
                school_year_id=sy.id,
                nucleos=NEIGHBORHOOD_CHOICES,
                teachers=teachers,
            )


@administration.route('/workshop/detail/<int:workshop_id>', methods=['GET'])
@login_required
def workshop_detail(workshop_id):
    workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
    return render_template('administration/workshop_detail.html', workshop=workshop)


@administration.route('/administration/map', methods=['GET'])
@login_required
def show_map():
    return render_template('administration/map.html')



@administration.route('/workshop/list', methods=['GET'])
@login_required
def workshop_list():
    pass


# @administration.route('/workshop/add-lesson/<int:workshop_id>', methods=['POST'])
# # @login_required
# def workshop_add_leson(workshop_id):
#     workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
#     form = LessonCreateForm(request.form)
#     if request.method == "POST" and form.validate():
#         lesson = Lesson.create()
#         workshop.add_lesson()
#     return render_template('administration/workshop_detail.html', workshop=workshop)



@administration.route('/workshop/students-list/<int:workshop_id>', methods=['GET'])
@login_required
def show_workshop_students(workshop_id):
    pass
