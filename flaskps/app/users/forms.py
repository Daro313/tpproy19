from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    SelectField,
)


class CreateFormUser(Form):
    email = StringField('Email', [validators.Email(), validators.InputRequired()])
    username = StringField('Nombre de usuario', [validators.InputRequired()])
    name =StringField('Nombre', [validators.InputRequired()])
    surname = StringField('Apellido', [validators.InputRequired()])
    password = StringField('Password', [validators.InputRequired()])
    active = BooleanField('Activo')
    roles = StringField('Roles',[validators.InputRequired()])
