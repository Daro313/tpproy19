from flaskps import db

from sqlalchemy_utils import ChoiceType

from .contants import SCHOOL_YEAR_CHOICES
from flaskps.utils.functions import get_today

__all__ = [
   'SchoolYear',
   'Workshop',
]


class SchoolYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, default=get_today())
    end_date = db.Column(db.Date, default=get_today())
    semesters = db.Column(ChoiceType(SCHOOL_YEAR_CHOICES))
    workshops = db.relationship(
            'Workshop', backref='semester', lazy=True)

    @classmethod
    def create(cls, form):
        start_date = form.start_date.data
        end_date = form.end_date.data
        semesters = form.semester.data
        instance = cls(start_date=start_date,end_date=end_date,semesters=semesters)

        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return instance

    def add_workshop(self, workshops):
        for workshop in workshops:
            self.workshops.append(workshops)


class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    short_name = db.Column(db.String(60))
    semester_id = db.Column(
        db.Integer, db.ForeignKey('school_year.id'), nullable=False)
