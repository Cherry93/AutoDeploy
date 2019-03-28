from Base import Base
from main.model.Project import projects

class ProjectService(Base):
    __model__ = projects
projectService = ProjectService()