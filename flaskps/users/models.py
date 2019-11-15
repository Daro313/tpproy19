from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
  
from flaskps import db, login_manager
from flaskps.utils.models import TimeStampedModel


class User(db.Model, TimeStampedModel, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)

    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))

    active = db.Column(db.Boolean, default=True) 
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Usuario: %r>' % self.username

    @property
    def is_active(self):
        return self.active

    @property
    def password(self):
        """
        Impide que se pueda leer la clave de usuario
        """
        raise AttributeError('password: no es un atributo de lectura. :D')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    # TODO: descomentar y agregar funcionalidad despues de crear migracion
    # many-to-many
    # @property
    # def display_rol(self):
    #     return ' | '.join(str(self.rol))



class Rol(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'rol'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return '<Rol: {}>'.format(self.name)


#class Permission(db.Model):
#
#    __tablename__ = 'permissions'
#
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(60), unique=True)
#
#    def __repr__(self):
#        return '<Permiso: {}>'.format(self.name)
#
#
#
## Set up user_loader
#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))











# test many to many user role
tags = db.Table('tags',
        db.Column(
            'tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
        db.Column(
            'page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
    )

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship(
                'Tag',
                secondary=tags,
                lazy='subquery',
                backref=db.backref('pages', lazy=True),
            )

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
