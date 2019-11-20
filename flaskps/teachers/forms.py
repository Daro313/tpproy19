from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField
)


class CreateTeachersForm(Form):
    surname = StringField('Apellido', [validators.DataRequired()])
    name = StringField('Nombre', [validators.DataRequired()])
    birth_date = DateField('Fecha de nacimiento',format='%Y-%m-%d')
    locality = StringField('Localidad', [validators.DataRequired()])
    address = StringField('Direccion', [validators.DataRequired()])
    document_type = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')])
    document_number = StringField('Numero de documento', [validators.DataRequired()])
    phone = StringField('Telefono')
