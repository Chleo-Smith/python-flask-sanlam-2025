import uuid
from email.policy import default

from extensions import db


# SCHMEA
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    # allow us to convert movie object to dict
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }
