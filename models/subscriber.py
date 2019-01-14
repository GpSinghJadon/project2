from db import db
import datetime

class SubscriberModel(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    license_key = db.Column(db.String(80), db.Foreign_key('licenses.id'))
    license = db.relationship('LicenseModel')


    def __init__(self, name, license_key, email):
        self.name = name
        self.license_key = license_key
        self.email = email

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
