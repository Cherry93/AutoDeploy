from Base import Base
from main.model.Project import projects
from main.utils.git import Git
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
projectService = ProjectService()