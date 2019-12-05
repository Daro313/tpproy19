from flaskps import db

from sqlalchemy_utils import ChoiceType

from .contants import SCHOOL_YEAR_CHOICES
from flaskps.utils.functions import get_today

__all__ = [
   'SchoolYear',
   'Semester',
]


class SchoolYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, default=get_today())
    end_date = db.Column(db.Date, default=get_today())
    semesters = db.relationship(
        'Semester', backref='school_year', lazy=True)



class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, default=get_today())
    end_date = db.Column(db.Date, default=get_today())
    year_semester = db.Column(ChoiceType(SCHOOL_YEAR_CHOICES))
    school_year_id = db.Column(
        db.Integer, db.ForeignKey('school_year.id'), nullable=False)
