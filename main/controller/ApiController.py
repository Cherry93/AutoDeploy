from main import app,logger
from flask import request,session,jsonify
from main.service.HostService import hostService
from main.service.DictService import dictService
from main.service.OperLogService import operLogService
from main.service.ProjectService import projectService
from main.service.UserService import userService
from .UserController import authorize

@app.route('/api/project/list/<int:id>')
@authorize(value=0)
def dict_projects(id):
    projects = projectService.find(dict_id=id).all()
    return jsonify(dict(code=200,data=projects))

@app.route("/api/projects/<int:id>/branches")
@authorize(value=1)
def api_project_branches(id):
    print(id)
    project = projectService.get(id)
    print(project)
    projectService.git_clone(project)
    return jsonify(dict(code=200, data=projectService.git_branch(project)))

@app.route("/api/projects/<int:id>/branches/<branch>/commits", methods=["GET"])
@authorize(value=1)
def project_branch_commits(id, branch):
    print(id)
    project = projectService.get(id)
    print(project)
    projectService.git_clone(project)
    return jsonify(dict(rc=0,
                        data=projectService.git_branch_commit_log(project, branch)))