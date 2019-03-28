from main import app
from main.service.ProjectService import projectService
from main.service.OperLogService import operLogService
from flask import request,session

@app.route('/project/all/<int:id>',methods=["GET"])
def projects(id):
    dict = {'dict_id':id}
    list = projectService.find(**dict).first()
    return


@app.route('/project/add',methods=["POST"])
def addproject():
    # add Project Name
    operLogService.addOper_log(username=session.get('username'),comment="Add Project")
    param = request.form.to_dict()
    projectService.create(**param)

@app.route('/project/edit/<int:id>',methods=["POST"])
def editproject(id):
    # oldProject -> newProject
    operLogService.addOper_log(username=session.get('username'),comment="Edit Project")
    param = request.form.to_dict()
    projectService.update(projectService.get(id=id),**param)

@app.route('/project/delete',methods=["POST"])
def deleteproject():
    pass