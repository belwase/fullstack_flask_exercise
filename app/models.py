from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    birthday = db.Column(db.String(64))
    salary = db.Column(db.Integer)
    description = db.Column(db.String(120))