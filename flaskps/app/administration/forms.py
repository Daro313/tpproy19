from wtforms import (
    Form,
    StringField,
    validators,
    DateField,
    SelectField,
)


class CreateSchoolYearForm(Form):
    start_date = DateField('Fecha de inicio', [
                validators.Length(min=6, max=35),
                validators.DataRequired()
            ])

    end_date = DateField('Fecha de fin', [validators.DataRequired()])
    semester = StringField('Semestre', [validators.DataRequired()])

