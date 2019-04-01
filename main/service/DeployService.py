from Base import Base
from main.model.Deploy import deploys
from main.service.ProjectService import projectService
from main.service.HostService import hostService
from main.service.ProjectHostService import projectHostService
from main.utils.git import Git

class DeployService(Base):
    __model__ = deploys
    def deploy(self,form):
        project = projectService.get(form.project_id)
        git  = Git(project.name,project.repo_url)
        # clone
        git.clone()
        # checkout
        git.checkout_branch(form.branch,form.commit)
        # deploy
        git.package(form.branch)
        # rsync
        # rsync -avzq --rsh="sshpass -p itcast ssh -p 22"
        # /home/dongmengyuan/deployProjects/SpringBootTest/target/demo-0.0.1-SNAPSHOT.jar
        # itcast@172.20.10.2:/home/itcast/Desktop/deployProjects/
        pass
deployService = DeployService()