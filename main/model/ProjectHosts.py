from main import db
from main.utils.jsonencoder import JsonSerializer

class projecthosts(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    project_id = db.Column(db.BIGINT)
    host_id = db.Column(db.BIGINT)