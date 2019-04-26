from Base import Base
from main.model.Project import projects
from main.utils.git import Git
from DictService import dictService
class ProjectService(Base):
    __model__ = projects
    def git_clone(self, project):
        git = Git(project.name, project.repo_url)
        git.clone()

    def git_branch(self, project):
        git = Git(project.name, project.repo_url)
        return git.remote_branch()

    def git_branch_commit_log(self, project, branch):
        git = Git(project.name, project.repo_url)
        git.checkout_branch(branch)
        return git.log()

    def dict_projects(self):
        projects = self.all(order_by="dict_id")
        projectdicts = {}
        for project in projects:
            Dict = dictService.get(project.dict_id)
            if projectdicts.has_key(Dict.name):
                list = projectdicts[Dict.name]
                list.append(project)
                projectdicts[Dict.name] = list
            else:
                list = []
                list.append(project)
                projectdicts[Dict.name] = list
        return projectdicts
projectService = ProjectService()