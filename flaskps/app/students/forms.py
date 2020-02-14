from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    IntegerField
)


from .constants import (
    GENDER_CHOICES,
)

class CreateStudentsForm(Form):
    surname = StringField('Apellido', [validators.DataRequired(message='Este es un campo requerido')])
    name = StringField('Nombre', [validators.DataRequired(message='Este es un campo requerido')])
    birth_date = DateField('Fecha de nacimiento', [validators.DataRequired(message='Este es un campo requerido')], format='%d-%m-%Y')
    borned = StringField('Lugar de nacimiento')
    locality = StringField('Localidad', [validators.DataRequired(message='Este es un campo requerido')])
    address = StringField('Direccion', [validators.DataRequired(message='Este es un campo requerido')])
    neighborhood = StringField('Barrio', [validators.DataRequired(message='Este es un campo requerido')])
    gender = SelectField('Genero', [validators.DataRequired(message='Este es un campo requerido')], choices=GENDER_CHOICES)
    document_type = StringField('Tipo de documento', [validators.DataRequired(message='Este es un campo requerido')])
    document_number = StringField('Numero de documento', [validators.DataRequired(message='Este es un campo requerido')])
    tutor = StringField('Tutor', [validators.DataRequired(message='Este es un campo requerido')])
    phone = IntegerField('Telefono', [validators.DataRequired(message='Solo se permite ingresar numeros')])
    school = StringField('Escuela', [validators.DataRequired(message='Este es un campo requerido')])
    level = StringField('Nivel', [validators.DataRequired(message='Este es un campo requerido')])
    tutor_name = StringField('apellido', [validators.DataRequired(message='Este es un campo requerido')])
