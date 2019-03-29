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

# @app.route('/admin/user/role/<int:id>/<int:role>',methods=["GET"])
# @authorize(value=2)
# def editRole(id,role):
#     userService.update(userService.get(id),role=role)
#     return jsonify(dict(msg="success"))

# host
@app.route('/host/all',methods=["GET"])
@authorize(value=2)
def list():
    list = hostService.all()
    return jsonify(dict(data=list))

@app.route('/host/add',methods=["POST"])
@authorize(value=2)
def addhost():
    # add Host ip
    param = request.form.to_dict()
    host = hostService.create(**param)
    user = session.get("user")
    logger.info("userId is %s add host,hostInfo is %s",
                user[u'id'], str(host))
    return jsonify(dict(code=200))

# @app.route('/host/delete/<id>',methods=["POST"])
# @authorize(value=2)
# def delete(id):
#     host = hostService.get(id)
#     user = session.get("user")
#     operLogService.addOper_log(deploy_id=None, id=user[u'id'], username=user[u'name'],
#                                comment="delete Host" + host[u'host_ip'])
#     hostService.delete(host)
#     return jsonify(dict(code=200))

# @app.route('/host/edit/<int:id>',methods=["POST"])
# @authorize(value=2)
# def edithost(id):
#     # oldHost -> newHost
#     operLogService.addOper_log(username=session.get('username'),comment="Edit Host")
#     param = request.form.to_dict()
#     hostService.update(hostService.get(id=id),**param)
#     return

# # dict
# @app.route('/dict/all',methods=["GET"])
# @authorize(value=2)
# def all():
#     list = dictService.all()
#     return jsonify(dict(code=200,data=list))
#
# @app.route('/dict/add',methods=["POST"])
# @authorize(value=2)
# def add():
#     # add dict Name
#     user = session.get("user")
#     operLogService.addOper_log(deploy_id=None,id=user[u'id'], username=user[u'name'],
#                                comment="add Dict" + request.form.get("name"))
#     param = request.form.to_dict()
#     dictService.create(**param)
#     return jsonify(dict(code=200))
#
# @app.route('/dict/edit/<int:id>',methods=["POST"])
# @authorize(value=2)
# def edit(id):
#     # oldName -> newName
#     operLogService.addOper_log(username=session.get('username'),comment="Edit Dict from to ")
#     param = request.form.to_dict()
#     dictService.update(dictService.get(id=id),**param)
#     return
#
# # project
# @app.route('/project/all/<int:id>',methods=["GET"])
# @authorize(value=2)
# def projects(id):
#     dict = {'dict_id':id}
#     list = projectService.find(**dict).first()
#     return
#
#
# @app.route('/project/add',methods=["POST"])
# def addproject():
#     # add Project Name
#     operLogService.addOper_log(username=session.get('username'),comment="Add Project")
#     param = request.form.to_dict()
#     projectService.create(**param)
#
# @app.route('/project/edit/<int:id>',methods=["POST"])
# def editproject(id):
#     # oldProject -> newProject
#     operLogService.addOper_log(username=session.get('username'),comment="Edit Project")
#     param = request.form.to_dict()
#     projectService.update(projectService.get(id=id),**param)
#
# @app.route('/project/delete',methods=["POST"])
# def deleteproject():
#     pass