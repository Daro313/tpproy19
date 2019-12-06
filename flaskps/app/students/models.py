from flaskps import db
from sqlalchemy_utils import ChoiceType
from .constants import (
    GENDER_CHOICES,
    LEVEL_CHOICES,
    NEIGHBORHOOD_CHOICES,
)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(60))
    name = db.Column(db.String(60))
    birth_date = db.Column(db.String(60))
    borned = db.Column(db.String(60))
    locality = db.Column(db.String(60))
    address = db.Column(db.String(60))
    neighborhood = db.Column(ChoiceType(NEIGHBORHOOD_CHOICES))
    gender = db.Column(ChoiceType(GENDER_CHOICES))
    document_type = db.Column(db.String(60))
    document_number = db.Column(db.String(60))
    tutor = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    school = db.Column(db.String(60))
    level = db.Column(ChoiceType(LEVEL_CHOICES))

    def __repr__(self):
        return '<Estudiante: %r>' % self.name

    def update(self, form):
        self.name = form.name.data
        self.surname = form.surname.data
        self.birth_date = form.birth_date.data
        self.borned = form.borned.data
        self.locality = form.locality.data
        self.address = form.address.data
        self.neighborhood = form.neighborhood.data
        self.gender = form.gender.data
        self.document_type = form.document_type.data
        self.document_number = form.document_number.data
        self.tutor = form.tutor.data
        self.phone = form.phone.data
        self.school = form.school.data
        self.level = form.level.data

        db.session.commit()

    def have_permissions(self, permission):
        perm = []
        for rol in self.roles:
            perm += rol.permisos.split(',')
        if permission in perm:
            return True
        return False
