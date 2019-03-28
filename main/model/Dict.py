from main import db

class dicts(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)