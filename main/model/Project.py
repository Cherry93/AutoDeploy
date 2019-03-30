from main import db
from main.utils.jsonencoder import JsonSerializer
class projects(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.VARCHAR)
    repo_url = db.Column(db.VARCHAR)
    dict_id = db.Column(db.BIGINT)
    create_date = db.Column(db.DATETIME)

    def __str__(self):
        return "project project_id is %s,name is %s,repo_url: %s, dict_id: %s" % (self.id, self.name,self.repo_url,self.dict_id)