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
