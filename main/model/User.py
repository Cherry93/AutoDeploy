from main import db

class users(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    role = db.Column(db.Integer)
    email = db.Column(db.VARCHAR)
    create_date = db.Column(db.DATE)
