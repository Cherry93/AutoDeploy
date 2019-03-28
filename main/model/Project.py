from main import db

class projects(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)
    repo_url = db.Column(db.VARCHAR)
    dict_id = db.Column(db.BIGINT)
    create_date = db.Column(db.DATE)