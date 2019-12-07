from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField
)


image        = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])


class CreateTeachersForm(Form):
    name = StringField('Nombre', [validators.DataRequired()])
    type = SelectField('Tipo', [validators.DataRequired()])
    inventory_number = StringField('Numero de documento', [validators.DataRequired()])
    image = FileField(u'Imagen', [validators.regexp(u'^[^/\\]\.jpg$')])
