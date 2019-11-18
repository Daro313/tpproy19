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
    birth_date = DateField('fecha de nacimiento', [validators.DataRequired()])
    borned = StringField('lugar de nacimiento')
    locality = StringField('Localidd', [validators.DataRequired()])
    address = StringField('Direccion', [validators.DataRequired()])
    neighborhood = SelectField('Barrio', choices=NEIGHBORHOOD_CHOICES)
    gender = SelectField('Genero', choices=GENDER_CHOICES)
    document_type = StringField('tipo de documento', [validators.DataRequired()])
    document_number = StringField('numero de documento', [validators.DataRequired()])
    tutor = StringField('tutor', [validators.DataRequired()])
    phone = StringField('teleforno')
    school = StringField('escuela', [validators.DataRequired()])
    level = SelectField('nivel', choices=LEVEL_CHOICES)

surname = 'otero'
name = 'mariano'
birth_date = '7/5/1988'
borned = 'bahia blanca'
locality = 'La plata'
address = '41 1492'
neighborhood = 1
gender = 'male'
document_type = 'DNI'
document_number = '33870338'
tutor = 'Juan Topo'
phone = '2216166842'
school = 'UNLP'
level = 1
