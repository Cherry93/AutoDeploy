from Base import Base
from main.model.Host import hosts

class HostService(Base):
    __model__ = hosts
hostService = HostService()