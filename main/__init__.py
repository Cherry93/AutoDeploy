from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask(__name__,template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1322762504@localhost:3306/AutoDeploy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
app.config['SECRET_KEY']="123456"
db = SQLAlchemy(app)
db_session = db.session

from .controller import UserController,DictController,HostController,ProjectController