from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    SelectField
)


class CreateFormUser(Form):
    email = StringField('Email', [
                validators.Length(min=6, max=35),
                validators.DataRequired()
            ])

    username = StringField('Nombre de usuario', [validators.DataRequired()])
    name =StringField('Nombre', [validators.DataRequired()])
    surname = StringField('Apellido', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
    active = BooleanField('Activo')
    roles = StringField('Rol', [validators.DataRequired()])

# class UpdateFormUser(Form):
#     email = StringField('Email', [
#                 validators.Length(min=6, max=35),
#                 validators.DataRequired()
#             ])
#
#     user_name = StringField('nombre de usuario', [validators.DataRequired()])
#     first_name =StringField('nombre', [validators.DataRequired()])
#     last_name = StringField('apellido', [validators.DataRequired()])
#     password = StringField('password', [validators.DataRequired()])
#     roles = StringField('rol', [validators.DataRequired()])
