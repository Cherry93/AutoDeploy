from main import app,logger
from flask import request,session,jsonify,render_template
from main.service.HostService import hostService
from main.service.DictService import dictService
from main.service.DeployService import deployService
from main.service.ProjectService import projectService
from main.service.ProjectHostService import projectHostService
from main.service.UserService import userService
from .UserController import authorize

@app.route('/api/dict/project/list')
@authorize(value=1)
def dict_projects():
    projects = projectService.all(order_by="dict_id")
    projectdicts = {}
    for project in projects:
        Dict = dictService.get(project.dict_id)
        if projectdicts.has_key(Dict.name):
            list = projectdicts[Dict.name]
            list.append(project)
            projectdicts[Dict.name]=list
        else:
            list = []
            list.append(project)
            projectdicts[Dict.name] = list
    return render_template('deploy.html',projectdicts=projectdicts,user=session['user'])

@app.route('/api/project/info/<int:id>')
@authorize(value=1)
def project_info(id):
    projecthosts = projectHostService.find(project_id=id).all()
    hostids = []
    for projecthost in projecthosts:
        hostids.append(projecthost.host_id)
    hosts=hostService.getByIds(hostids)
    return render_template('projectInfo.html',hosts=hosts,user=session['user'],projectdicts=projectService.dict_projects())

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

@app.route("/api/deploys", methods=["GET"])
# @authorize(value=1)
def api_post_deploy():
    form = DeployForm()
    form.project_id = request.args.get("project_id",type=int)
    form.branch = request.args.get("branch")
    form.commit = request.args.get("commit")
    # form.project_id = request.form.get("project_id",type=int)
    # form.branch = request.form.get("branch")
    # form.commit = request.form.get("commit")
    deployService.deploy(form)
    return jsonify(dict())

class DeployForm():
    pass