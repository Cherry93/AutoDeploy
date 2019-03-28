from main import app
from main.service.HostService import hostService
from main.service.OperLogService import operLogService
from flask import jsonify
from flask import request,session

@app.route('/host/all',methods=["GET"])
def list():
    list = hostService.all()
    return jsonify(dict(data=list))

@app.route('/host/add',methods=["POST"])
def addhost():
    # add Host ip

    operLogService.addOper_log(username=session.get('username'),comment="Add Host ()")
    param = request.form.to_dict()
    hostService.create(**param)

@app.route('/host/delete/<id>',methods=["POST"])
def delete(id):
    pass

@app.route('/host/edit/<int:id>',methods=["POST"])
def edithost(id):
    # oldHost -> newHost
    operLogService.addOper_log(username=session.get('username'),comment="Edit Host")
    param = request.form.to_dict()
    hostService.update(hostService.get(id=id),**param)
    return