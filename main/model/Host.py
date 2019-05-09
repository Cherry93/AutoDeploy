from main import db
from main.utils.jsonencoder import JsonSerializer
class hosts(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    host_ip = db.Column(db.VARCHAR)
    ssh_username = db.Column(db.VARCHAR)
    ssh_password = db.Column(db.VARCHAR)
    ssh_port = db.Column(db.Integer)

    def __str__(self):
        return "host host_id is %s,host_ip: %s, ssh_username: %s,ssh_password : %s" % (self.id, self.host_ip,self.ssh_username,self.ssh_password)