from main import db
from main.utils.jsonencoder import JsonSerializer
from datetime import datetime

class users(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    role = db.Column(db.Integer)
    email = db.Column(db.VARCHAR)
    create_date = db.Column(db.DATETIME)

    def __str__(self):
        return "user user_id: %d, user_name: %s,role : %s,email is %s" % (self.id, self.name,self.role,self.email)
