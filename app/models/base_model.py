from app.app import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    created = db.Column(db.DateTime, default=datetime.now())
    updated = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    is_deleted = db.Column(db.Boolean, default=False)
