from db import db
import datetime

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    device_id = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, device_id):
        self.name = name
        self.device_id = device_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_device_id(cls, device_id):
        return cls.query.filter_by(device_id=device_id).first()

    def json(self):
        return {"name":self.name, "device_id":self.device_id}