from main import db
from main.utils.jsonencoder import JsonSerializer
class deploys(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    project_id = db.Column(db.BIGINT)
    host_id = db.Column(db.BIGINT)
    branch = db.Column(db.VARCHAR)
    status = db.Column(db.Integer)
