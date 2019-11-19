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
    surname = StringField('apellido', [validators.DataRequired()])
    name = StringField('nombre', [validators.DataRequired()])
    birth_date = DateField('fecha de nacimiento', [validators.DataRequired()],format='%Y-%m-%d')
    locality = StringField('Localidd', [validators.DataRequired()])
    address = StringField('Direccion', [validators.DataRequired()])
    document_type = StringField('tipo de documento', [validators.DataRequired()])
    document_number = StringField('numero de documento', [validators.DataRequired()])
    phone = StringField('teleforno')
