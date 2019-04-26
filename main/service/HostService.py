from Base import Base
from main.model.Host import hosts

class HostService(Base):
    __model__ = hosts

    def getByIds(self,ids):
        query = self.session.query(self.__model__)
        return query.filter(self.__model__.id.in_(ids)).all()
    def batchGet(self,ids):
        return self.session.query(self.__model__).filter_by(self.__model__.id.in_(ids)).all()
hostService = HostService()