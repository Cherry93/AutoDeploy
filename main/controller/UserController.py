# -*- coding:utf-8 -*-
from main import app
from main.service.UserService import userService
from main.service.OperLogService import operLogService
from flask import request,session
from flask import render_template,jsonify
from flask import make_response
from datetime import datetime
from functools import wraps

def authorize(value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            user = session.get("user")
            if user is None:
                return render_template('login.html',message="登录已经过期,请重新登录")
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
        user.password = None
        session['user'] = user
        if user.role == 2:
            return render_template('main.html', user = user)
        else:
            return render_template('Welcome.html',user=user)
    else:
        message = "username not matched password"
        return render_template('login.html',message = message)

@app.route('/oper')
@authorize(value=1)
def oper():
    user = session.get("user")
    operLogService.create(user_id=user[u'id'],username=user[u'name'],comment="oper",create_date=datetime.now())
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('login.html')


@app.route('/user/page')
def userpage():
    return render_template('user.html',user=session['user'])

@app.route('/project/page')
def propage():
    return render_template('project.html',user=session['user'])

@app.route('/host/page')
def hostpage():
    return render_template('host.html',user=session['user'])

@app.route('/dict/page')
def dictpage():
    return render_template('dict.html',user=session['user'])
