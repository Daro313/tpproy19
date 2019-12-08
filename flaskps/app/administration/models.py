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


workshop_students = db.Table('workshop_students',
    db.Column(
        'workshop_id', db.Integer, db.ForeignKey('workshop.id'), primary_key=True),
    db.Column(
        'student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('attent_date', db.Date)
)


class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    short_name = db.Column(db.String(60))
    cant_lessons = db.Column(db.Integer, default=0)
    semester_id = db.Column(
        db.Integer, db.ForeignKey('school_year.id'), nullable=False)
    teacher_id = db.Column(
        db.Integer, db.ForeignKey('teachers.id'), nullable=True)
    students = db.relationship(
                    'Students',
                    secondary=workshop_students,
                    lazy='subquery',
                    backref=db.backref('workshops', lazy=True)
                )

class AttendWorkshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))


