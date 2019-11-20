from flaskps import db
import datetime

def _get_date():
    return datetime.datetime.now()

class TimeStampedModel():
    created_at = db.Column(db.Date, default=_get_date)
    updated_at = db.Column(db.Date, onupdate=_get_date)


