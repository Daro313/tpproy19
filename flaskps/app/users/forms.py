from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    SelectField,
)


class CreateFormUser(Form):
    email = StringField('Email', [validators.Email(), validators.InputRequired(message='Campo requerido')])
    username = StringField('Nombre de usuario', [validators.InputRequired(message='Campo requerido')])
    name =StringField('Nombre', [validators.InputRequired(message='Campo requerido')])
    surname = StringField('Apellido', [validators.InputRequired(message='Campo requerido')])
    password = StringField('Password', [validators.InputRequired(message='Campo requerido')])
    active = BooleanField('Activo')
    roles = StringField('Roles',[validators.InputRequired(message='Campo requerido')])
