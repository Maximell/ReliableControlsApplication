from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model for storing devices and their associated counts
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(db.String(80), unique=True, nullable=False)
    faultCount = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "deviceId": self.deviceId,
            "faultCount": self.faultCount
        }

    def __repr__(self):
        return '<Device %r>' % self.deviceId
