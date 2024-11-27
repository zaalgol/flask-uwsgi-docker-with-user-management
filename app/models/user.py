from app.app import db
from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Increased length for hashed passwords
    latest_login = db.Column(db.DateTime, nullable=True)
