from Base import Base
from main.model.OperLog import oper_log
from datetime import datetime

class OperLogService(Base):
    __model__ = oper_log

    def addOper_log(self,deploy_id, id, username, comment):
        log = oper_log()
        log.deploy_id = deploy_id
        log.user_id = id
        log.username = username
        log.comment = comment
        log.create_date = datetime.now()
        self.save(log)
operLogService = OperLogService()



