from db import db
import datetime

class LicenseModel(db.Model):
    __tablename__ = 'licenses'

    license_key = db.Column(db.DateTime, primary_key=True)
    start_date = db.Column(db.DateTime, default= datetime.datetime.now)
    expiry_date = db.column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


    def __init__(self, license_key, expiry_date):
        self.license_key = license_key
        self.expiry_date = expiry_date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_license_key(cls, license_key):
        return cls.query.filter_by(license_key=license_key).first()
