from wtforms import (
    Form,
    StringField,
    validators,
    DateField,
    SelectField,
    IntegerField,
)

from .contants import SCHOOL_YEAR_CHOICES


class CreateSchoolYearForm(Form):
    start_date = DateField('Fecha de inicio', [ validators.DataRequired() ])
    end_date = DateField('Fecha de fin', [validators.DataRequired()])
    semester = SelectField('Semestre', [validators.DataRequired()], choices=SCHOOL_YEAR_CHOICES)


class WorkshopCreateForm(Form):
    name = StringField('Nombre', [validators.DataRequired()])
    short_name = StringField('Nombre corto', [validators.DataRequired()])
    # semester = StringField('semestre', [validators.DataRequired()])
    teacher = StringField('Maestre', [validators.DataRequired()])
    nucleo = StringField('Nucleo', [validators.DataRequired()])
    address = StringField('Direccion', [validators.DataRequired()])
    horario = StringField('Horario', [validators.DataRequired()])
    days = StringField('dias', [validators.DataRequired()])
    clases = IntegerField('clases', [validators.DataRequired()])

    


