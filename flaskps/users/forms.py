from wtforms import Form, BooleanField, StringField, PasswordField, validators


class CreateFormUser(Form):
    email = StringField('Email', [
                validators.Length(min=6, max=35),
                validators.DataRequired()
            ])

    user_name = StringField('nombre de usuario', [validators.DataRequired()])
    first_name =StringField('nombre', [validators.DataRequired()])
    last_name = StringField('apellido', [validators.DataRequired()])
    password = StringField('password', [validators.DataRequired()])
    roles = StringField('rol', [validators.DataRequired()])

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
