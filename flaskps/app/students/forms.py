from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField
)


from .constants import (
    GENDER_CHOICES,
    LEVEL_CHOICES,
    NEIGHBORHOOD_CHOICES,
)

class CreateStudentsForm(Form):
    surname = StringField('apellido', [validators.DataRequired()])
    name = StringField('nombre', [validators.DataRequired()])
    birth_date = DateField('fecha de nacimiento', [validators.DataRequired()], format='%Y-%m-%d')
    borned = StringField('lugar de nacimiento')
    locality = StringField('Localidd', [validators.DataRequired()])
    address = StringField('Direccion', [validators.DataRequired()])
    neighborhood = SelectField('Barrio', [validators.DataRequired()], choices=NEIGHBORHOOD_CHOICES)
    gender = SelectField('Genero', [validators.DataRequired()], choices=GENDER_CHOICES)
    document_type = StringField('tipo de documento', [validators.DataRequired()])
    document_number = StringField('numero de documento', [validators.DataRequired()])
    tutor = StringField('tutor', [validators.DataRequired()])
    phone = StringField('teleforno')
    school = StringField('escuela', [validators.DataRequired()])
    level = SelectField('nivel', [validators.DataRequired()], choices=LEVEL_CHOICES)
    tutor_name = StringField('apellido', [validators.DataRequired()])
