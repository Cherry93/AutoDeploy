from main import app
from main.service.UserService import userService
from flask import request,session
from flask import render_template
from flask import make_response

@app.route('/login',methods=["POST"])
def login():
    dict = request.form.to_dict()
    user = userService.find(**dict).first()
    if user is not None:
        response = make_response(render_template('Welcome.html',user=user))
        # response.set_cookie('token',user.name)
        session['username'] = user.name

        return response
    else:
        message = "username not matched password"
        return render_template('login.html',message = message)

@app.route('/oper')
def oper():
    # name = request.cookies.get("token")
    name = session.get("username")
    if name is not None:
        return render_template('login.html',message=name)
    else:
        message = "token is expired"
        return render_template('login.html',message=message)


@app.route('/index')
def index():
    return render_template('login.html')