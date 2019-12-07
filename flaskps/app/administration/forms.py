from wtforms import (
    Form,
    StringField,
    validators,
    DateField,
    SelectField,
)

from .contants import SCHOOL_YEAR_CHOICES


class CreateSchoolYearForm(Form):
    start_date = DateField('Fecha de inicio', [ validators.DataRequired() ])
    end_date = DateField('Fecha de fin', [validators.DataRequired()])
    semester = SelectField('Semestre', [validators.DataRequired()], choices=SCHOOL_YEAR_CHOICES)

