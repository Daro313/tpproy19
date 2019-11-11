from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flaskps import db, login_manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class UserProfile(User):
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    active = db.Column(db.Boolean, default=True)
    roles = ,  
       children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")


class Role():
    id = db.Column(db.Integer, primary_key=True)




https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Child", back_populates="parents")
    parent = relationship("Parent", back_populates="children")

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Association", back_populates="parent")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship("Association", back_populates="child")
