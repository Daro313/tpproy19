from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    IntegerField,
)


class CreateTeachersForm(Form):
    surname = StringField('Apellido', [validators.DataRequired(message='Este es un campo requerido')])
    name = StringField('Nombre', [validators.DataRequired(message='Este es un campo requerido')])
    birth_date = DateField('Fecha de nacimiento', [validators.DataRequired(message='Este es un campo requerido')], format='%d-%m-%Y')
    locality = StringField('Localidad', [validators.DataRequired(message='Este es un campo requerido')])
    address = StringField('Direccion', [validators.DataRequired(message='Este es un campo requerido')])
    document_type = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')])
    document_number = StringField('Numero de documento', [validators.DataRequired(message='Este es un campo requerido')])
    phone = IntegerField('Telefono', [validators.DataRequired(message='Solo se permite ingresar numeros')])
