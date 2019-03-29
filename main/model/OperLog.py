from main import db
from main.utils.jsonencoder import JsonSerializer
class oper_log(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    deploy_id = db.Column(db.BIGINT)
    user_id = db.Column(db.BIGINT)
    username = db.Column(db.VARCHAR)
    comment = db.Column(db.VARCHAR)
    create_date = db.Column(db.DateTime)