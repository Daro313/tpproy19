from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    FileField,
)

from .constants import INSTRUMENT_TYPES

class CreateInstrumentsForm(Form):
    name = StringField('Nombre', [validators.DataRequired()])
    type = SelectField('Tipo', [validators.DataRequired()], choices=INSTRUMENT_TYPES)
    inventory_number = StringField('Numero de inventario', [validators.DataRequired()])
