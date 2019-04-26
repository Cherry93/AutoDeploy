# -*- coding:utf-8 -*-
from main import app
from main.service.UserService import userService
from main.service.OperLogService import operLogService
from main.service.ProjectService import projectService
from flask import request,session,jsonify
from flask import render_template
from datetime import datetime
from functools import wraps

def authorize(value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            user = session.get("user")
            if user is None:
                return render_template('login.html',message="login expired")
            if user[u'role'] >= value:
                return func(*args,**kwargs)
            else:
                return render_template("login.html",message="unable to access,Permission undenied")
        return wrapper
    return decorator

@app.route('/login',methods=["POST"])
def login():
    dict = request.form.to_dict()
    user = userService.first(**dict)
    if user is not None:
        user.password = ""
        session['user'] = user
        if user.role == 2:
            return render_template('main.html', user = user)
        else:
            return render_template('deploy.html',user=user,projectdicts=projectService.dict_projects())
    else:
        message = "username not matched password"
        return render_template('login.html',message = message)

@app.route('/logout')
def logout():
    session['user']=None
    return render_template('login.html')

@app.route('/oper')
@authorize(value=1)
def oper():
    return jsonify(dict(code=200))

@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/user/page')
@authorize(value=2)
def userpage():
    return render_template('user.html',user=session['user'])

@app.route('/project/page')
@authorize(value=2)
def propage():
    return render_template('project.html',user=session['user'])

@app.route('/host/page')
@authorize(value=2)
def hostpage():
    return render_template('host.html',user=session['user'])

@app.route('/dict/page')
@authorize(value=2)
def dictpage():
    return render_template('dict.html',user=session['user'])


