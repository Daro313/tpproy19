from flaskps import db
from sqlalchemy_utils import ChoiceType
from sqlalchemy_imageattach.entity import Image, image_attachment

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    inventory_number = db.Column(db.Integer)
    picture = image_attachment('InstrumentPicture')

    def __repr__(self):
        return '<Instrumento: %r>' % self.name

    def update(self, form):
        self.name = form.name.data
        self.type = form.type.data
        self.inventory_number = form.inventory_number.data

        db.session.commit()

    def have_permissions(self, permission):
        perm = []
        for rol in self.roles:
            perm += rol.permisos.split(',')
        if permission in perm:
            return True
        return False

class InstrumentPicture(db.Model, ):
    __tablename__ = 'instrument_pictures'
    id = db.Column(db.Integer, ForeingKey('instrument.id'), primary_key=True)
    instrument = relationship('Instrument')
