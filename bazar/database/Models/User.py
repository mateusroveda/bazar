from bazar.bootstrap.database import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    """ Data Model for Users Table"""
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)