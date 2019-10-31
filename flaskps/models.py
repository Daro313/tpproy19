from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flaskps import db, login_manager


# class TimeStampedModel(db.Model):
# 
#     class Meta:
#         abstract = True
# 
#     created_at = DateTimeField(
#         auto_now_add=True, null=True, blank=True, db_index=True)
# 
#     updated_at = DateTimeField(auto_now=True, null=True, blank=True)

roles = ['profesor', 'preceptor', 'admin']


class User(db.Model, UserMixin):
    """
    Create an User table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    # TODO: eliminar rol cuando se creen roles en el modelo
    # esto es una relacion role
    rol = db.Column(db.String(60), index=True)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        return self.active

    # @property
    # def display_rol(self):
    #     return ' | '.join(str(self.rol))

    def __repr__(self):
        return '<Usuario: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Courses(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    # users = db.relationship('User', backref='course', lazy='dynamic')

    def __repr__(self):
        return '<Courses: {}>'.format(self.name)
