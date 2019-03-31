from Base import Base
from main.model.ProjectHosts import projectHosts

class ProjectHostService(Base):
    __model__ = projectHosts

projectHostService = ProjectHostService()