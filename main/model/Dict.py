from main import db
from main.utils.jsonencoder import JsonSerializer
class dicts(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)