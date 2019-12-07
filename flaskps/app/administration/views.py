from flask_login import login_required
from flask import render_template, redirect, request, url_for

from . import administration
from .models import SchoolYear
from .forms import CreateSchoolYearForm


@administration.route('/school-year/create', methods=['GET', 'POST'])
# @login_required
def school_year_create():
    """
    metodo GET: renderiza form de creacion
    metodo POST: verifica los datos y crea usuaraio
    """
    form = CreateSchoolYearForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.validate())
        print(form.start_date)
        print(form.end_date)
        print(form.semester)
        school_year = SchoolYear.create(form)
        return render_template('administration/create.html')
        # return redirect(url_for('administration.school_year_detail', school_year_id=school_year.id))
    return render_template('administration/create.html')


@administration.route('/school-year/detail/<int:school_year_id>', methods=['GET'])
# @login_required
def school_year_detail(school_year_id):
    school_year = SchoolYear.query.filter_by(id=school_year_id).first()
    return render_template('administration/detail.html', shool_year=school_year)

