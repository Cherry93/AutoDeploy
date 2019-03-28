from main import db

class deploys(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    project_id = db.Column(db.BIGINT)
    host_id = db.Column(db.BIGINT)
    branch = db.Column(db.VARCHAR)
    status = db.Column(db.Integer)
    create_date = db.Column(db.DATE)