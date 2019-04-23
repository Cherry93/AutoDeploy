from Base import Base
from main.model.ProjectHosts import projecthosts

class ProjectHostService(Base):
    __model__ = projecthosts

projectHostService = ProjectHostService()