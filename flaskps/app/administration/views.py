from flask_login import login_required
from flask import render_template, redirect, request, url_for

from . import administration
from .models import SchoolYear
from .forms import CreateSchoolYearForm
from flaskps.app.configurations.models import Configurations


@administration.route('/school-year/create', methods=['GET', 'POST'])
# @login_required
def school_year_create():
    """
    metodo GET: renderiza form de creacion
    metodo POST: verifica los datos y crea usuaraio
    """
    form = CreateSchoolYearForm(request.form)
    if request.method == 'POST' and form.validate():
        school_year = SchoolYear.create(form)
        return redirect(url_for('administration.school_year_detail', school_year_id=school_year.id))
    return render_template('administration/create.html')


@administration.route('/school-year/detail/<int:school_year_id>', methods=['GET'])
# @login_required
def school_year_detail(school_year_id):
    school_year = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
    return render_template('administration/detail.html', school_year=school_year)

@administration.route('/school-year/list', methods=['GET'], defaults={'page':1})
@administration.route('/school-year/list/<int:page>', methods=['GET'])
def school_year_list(page):
    conf = Configurations.query.first()
    school_years = SchoolYear.query.filter_by().paginate(
                        page,
                        conf.offset_paginator,
                        False
                    )

    return render_template(
            'administration/school_year_list.html', school_years=school_years)

    
    
