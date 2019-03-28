from main import db

class oper_log(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    deploy_id = db.Column(db.BIGINT)
    username = db.Column(db.VARCHAR)
    comment = db.Column(db.VARCHAR)
    create_date = db.Column(db.DATE)