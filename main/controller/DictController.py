from main import app
from main.service.DictService import dictService
from main.service.OperLogService import operLogService
from flask import request,session
from flask import jsonify

@app.route('/dict/all',methods=["GET"])
def all():
    list = dictService.all()
    return jsonify(dict(rc=0,data=list))

@app.route('/dict/add',methods=["POST"])
def add():
    # add dict Name

    operLogService.addOper_log(username=session.get('username'),comment="Add Dict()")
    param = request.form.to_dict()
    dictService.create(**param)

@app.route('/dict/edit/<int:id>',methods=["POST"])
def edit(id):
    # oldName -> newName
    operLogService.addOper_log(username=session.get('username'),comment="Edit Dict from to ")
    param = request.form.to_dict()
    dictService.update(dictService.get(id=id),**param)
    return

