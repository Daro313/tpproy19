from flaskps import db

class Configurations(db.Model):
    """
    Crear modelo de configuariones
    """

    __tablename__ = 'configurations'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    description = db.Column(db.String(200))
    title = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), index=True)
    offset_paginator = db.Column(db.Integer, default=20)
