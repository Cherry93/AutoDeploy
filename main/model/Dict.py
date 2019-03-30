from main import db
from main.utils.jsonencoder import JsonSerializer
class dicts(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)

    def __str__(self):
        return "dict dict_id is %s,name: %s" % (self.id, self.name)