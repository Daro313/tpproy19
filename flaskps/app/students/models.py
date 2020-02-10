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
    # tutor_name = db.Column(db.String(60))

    def __repr__(self):
        return '<Estudiante: %r>' % self.name

    @classmethod
    def create(cls, form):
        instance = cls(
            name=form.name.data,
            surname=form.surname.data,
            birth_date=form.birth_date.data,
            borned=form.borned.data,
            locality=form.locality.data,
            address=form.address.data,
            neighborhood=form.neighborhood.data,
            gender=form.gender.data,
            document_type=form.document_type.data,
            document_number=form.document_number.data,
            tutor=form.tutor.data,
            phone=form.phone.data,
            school=form.school.data,
            level=form.level.data,
            # tutor_name=form.tutor_name,
        )
        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    @classmethod
    def delete(cls, student_id):
        student = Students.query.filter_by(id=student_id).first_or_404()
        db.session.delete(student)
        db.session.commit()

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
