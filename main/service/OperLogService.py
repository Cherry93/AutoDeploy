from Base import Base
from main.model.OperLog import oper_log

class OperLogService(Base):
    __model__ = oper_log

    def addOper_log(self, username, comment):
        log = oper_log()
        log.username = username
        log.comment = comment
        self.save(log)
operLogService = OperLogService()



