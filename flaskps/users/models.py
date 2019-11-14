from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
  
from flaskps import db, login_manager
from flaskps.utils.models import TimeStampedModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_rol = Table('user_rol', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class User(db.Model, TimeStampedModel, UserMixin):

    __tablename__ = 'users'

    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    active = db.Column(db.Boolean, default=True)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    rol = relationship("Role",
                secondary="user_rol",
                backref="users")

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


permission_rol = Table('permission_rol', Base.metadata,
    Column('permission_id', Integer, ForeignKey('permissions.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    permission = relationship("Permission",
                secondary="permission_rol",
                backref="roles")

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    def __repr__(self):
        return '<Permiso: {}>'.format(self.name)



# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
