from main import db

class hosts(db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    host_ip = db.Column(db.VARCHAR)
    ssh_username = db.Column(db.VARCHAR)
    ssh_password = db.Column(db.VARCHAR)
    create_date = db.Column(db.DATE)