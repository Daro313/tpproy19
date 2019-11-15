from flaskps import db

class Courses(db.Model):
    """
    Create a Courses table
    """

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    # users = db.relationship('User', backref='course', lazy='dynamic')

    def __repr__(self):
        return '<Courses: {}>'.format(self.name)
