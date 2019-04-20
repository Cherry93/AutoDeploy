from main import app,logger
from flask import request,session,jsonify
from main.service.HostService import hostService
from main.service.DictService import dictService
from main.service.OperLogService import operLogService
from main.service.ProjectService import projectService
from main.service.UserService import userService
from .UserController import authorize


# user
@app.route('/admin/user/add',methods=["POST"])
@authorize(value=2)
def addUser():
    data = request.form.to_dict()
    data["password"] = "123456"
    user = userService.create(**data)
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s add user,userInfo is %s",opertorId,str(user))
    return jsonify(dict(msg="success"))

@app.route('/admin/user/list')
@authorize(value=2)
def userList():
    offset = request.args.get("page", None, type=int)
    limit = request.args.get("limit", None, type=int)
    count = userService.count()
    all = userService.all(offset=offset,limit=limit,order_by=None,desc=False)
    return jsonify(dict(code=0,data=all,msg="",count=count))

@app.route('/admin/user/edit',methods=["POST"])
@authorize(value=2)
def editUser():
    userId = request.form.get("id")
    origin = userService.get(userId)
    originS = str(origin)
    userService.update(origin,**request.form.to_dict())
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s edit user,origin userInfo is %s,dest userInfo is %s",opertorId,originS,str(origin))
    return jsonify(dict(code=200))

@app.route('/admin/user/del/<int:id>')
@authorize(value=2)
def delUser(id):
    opertorId = session.get("user")[u'id']
    user = userService.get(id)
    userService.delete(user)
    logger.info("userId is %s del user,userInfo is %s",opertorId,str(user))
    return jsonify(dict(code=200))

# host
@app.route('/admin/host/all',methods=["GET"])
@authorize(value=2)
def hostList():
    offset = request.args.get("offset", None, type=int)
    limit = request.args.get("limit", None, type=int)
    list = hostService.all(offset=offset, limit=limit, order_by=None, desc=False)
    return jsonify(dict(code=200,data=list))

@app.route('/admin/host/add',methods=["POST"])
@authorize(value=2)
def addhost():
    # add Host ip
    param = request.form.to_dict()
    host = hostService.create(**param)
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s add host,hostInfo is %s",opertorId, str(host))
    return jsonify(dict(code=200))

@app.route('/admin/host/del/<id>')
@authorize(value=2)
def delHost(id):
    opertorId = session.get("user")[u'id']
    host = hostService.get(id)
    hostService.delete(host)
    logger.info("userId is %s del host,hostInfo is %s", opertorId, str(host))
    return jsonify(dict(code=200))

@app.route('/admin/host/edit',methods=["POST"])
@authorize(value=2)
def editHost():
    hostId = request.form.get("id")
    origin = hostService.get(hostId)
    originS = str(origin)
    hostService.update(origin, **request.form.to_dict())
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s edit host,origin hostInfo is %s,dest hostInfo is %s", opertorId, originS, str(origin))
    return jsonify(dict(code=200))

# dict
@app.route('/admin/dict/all',methods=["GET"])
@authorize(value=0)
def dictList():
    offset = request.args.get("offset", None, type=int)
    limit = request.args.get("limit", None, type=int)
    list = dictService.all(offset=offset, limit=limit, order_by=None, desc=False)
    return jsonify(dict(code=200, data=list))

@app.route('/admin/dict/add',methods=["POST"])
@authorize(value=2)
def addDict():
    # add dict Name
    param = request.form.to_dict()
    dictM = dictService.create(**param)
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s add host,hostInfo is %s", opertorId, str(dictM))
    return jsonify(dict(code=200))

@app.route('/admin/dict/edit',methods=["POST"])
@authorize(value=2)
def editDict():
    dictId = request.form.get("id")
    origin = dictService.get(dictId)
    originS = str(origin)
    dictService.update(origin, **request.form.to_dict())
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s edit dict,origin dictInfo is %s,dest dictInfo is %s", opertorId, originS, str(origin))
    return jsonify(dict(code=200))

@app.route('/admin/dict/del/<int:id>')
@authorize(value=2)
def delDict(id):
    opertorId = session.get("user")[u'id']
    dictM = dictService.get(id)
    userService.delete(dictM)
    logger.info("userId is %s del dict,dictInfo is %s",opertorId,str(dictM))
    return jsonify(dict(code=200))

# # project
@app.route('/admin/project/all',methods=["GET"])
@authorize(value=2)
def projectList():
    list = projectService.all()
    return jsonify(dict(code=200,data=list))

@app.route('/admin/project/add',methods=["POST"])
@authorize(value=2)
def addProject():
    param = request.form.to_dict()
    dictM = projectService.create(**param)
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s add project,projectInfo is %s", opertorId, str(dictM))
    return jsonify(dict(code=200))

@app.route('/admin/project/edit',methods=["POST"])
@authorize(value=2)
def editProject():
    dictId = request.form.get("id")
    origin = projectService.get(dictId)
    originS = str(origin)
    projectService.update(origin, **request.form.to_dict())
    opertorId = session.get("user")[u'id']
    logger.info("userId is %s edit project,origin projectInfo is %s,dest projectInfo is", opertorId, originS, str(origin))
    return jsonify(dict(code=200))

@app.route('/admin/project/del/<int:id>')
@authorize(value=2)
def delProject(id):
    opertorId = session.get("user")[u'id']
    dictM = projectService.get(id)
    userService.delete(dictM)
    logger.info("userId is %s del project,projectInfo is %s",opertorId,str(dictM))
    return jsonify(dict(code=200))