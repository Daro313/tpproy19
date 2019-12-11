from flaskps import db

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    inventory_number = db.Column(db.String(60))
    img_path = db.Column(db.String(120))

    def __repr__(self):
        return '<Instrumento: %r>' % self.name

    @classmethod
    def create(cls, form, path):
        name = form.name.data
        type = form.type.data
        inventory_number = form.inventory_number.data
        img_path = path
        instance = cls(name=name,type=type,inventory_number=inventory_number,img_path=img_path)


        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    def update(self, form, path):
        self.name = form.name.data
        self.type = form.type.data
        self.inventory_number = form.inventory_number.data
        self.img_path = path
        db.session.commit()
