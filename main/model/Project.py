from main import db
from main.utils.jsonencoder import JsonSerializer
class projects(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)
    repo_url = db.Column(db.VARCHAR)
    dict_id = db.Column(db.BIGINT)
    create_date = db.Column(db.DATE)