from Base import Base
from main.model.Deploy import deploys
from main.service.ProjectService import projectService
from main.service.HostService import hostService
from main.service.ProjectHostService import projectHostService
from main.utils.git import Git
import threading

class DeployService(Base):
    __model__ = deploys
    def deploy(self,form):
        dest = "/home/aaa/"
        project = projectService.get(form.project_id)
        git  = Git(project.name,project.repo_url)
        # clone
        git.clone()
        # checkout
        git.checkout_branch(form.branch,form.commit)
        # deploy
        git.package(form.branch)
        prohosts = projectHostService.find(project_id=form.project_id).all()
        for prohost in prohosts:
            host = hostService.get(prohost.host_id)
            cmd = ("rsync -avzq --include='target/' --include='target/*.jar' --exclude='*' --exclude='*/' "
                   "--rsh=\"sshpass -p {ssh_pass} ssh -p {ssh_port}\" "
                   " {local_dest}/ {ssh_user}@{ssh_host}:"
                   "{remote_dest}/")
            cmd = cmd.format(ssh_pass=host.ssh_password,
                       ssh_port=host.ssh_port,
                       local_dest=git.location+project.name,
                       ssh_user=host.ssh_username,
                       ssh_host=host.host_ip,
                       remote_dest=dest+project.name)
            git.deploy(cmd)
            model = self.__model__()
            model.host_id=host.id
            model.project_id=form.project_id
            model.branch=form.branch
            model = deployService.save(model=model)
        return model

        # rsync
        # rsync -avzq --rsh="sshpass -p itcast ssh -p 22"
        # /home/dongmengyuan/deployProjects/SpringBootTest/target/demo-0.0.1-SNAPSHOT.jar
        # itcast@172.20.10.2:/home/itcast/Desktop/deployProjects/
        #rsync - anvz - i - -include = 'target/' - -include = 'target/*.jar' - -exclude = '*' - -exclude = '*/' / home / itcast / Desktop / deployProjects / Deploy / / home / itcast

    def rollback(self,form):
        dest = "/home/aaa/"
        project = projectService.get(form.project_id)
        git = Git(project.name, project.repo_url)
        # checkout
        git.rollback()
        # deploy
        git.package(form.branch)
        prohosts = projectHostService.find(project_id=form.project_id).all()
        for prohost in prohosts:
            host = hostService.get(prohost.host_id)
            cmd = ("rsync -avzq --include='target/' --include='target/*.jar' --exclude='*' --exclude='*/' "
                   "--rsh=\"sshpass -p {ssh_pass} ssh -p {ssh_port}\" "
                   " {local_dest}/ {ssh_user}@{ssh_host}:"
                   "{remote_dest}/")
            cmd = cmd.format(ssh_pass=host.ssh_password,
                             ssh_port=host.ssh_port,
                             local_dest=git.location + project.name,
                             ssh_user=host.ssh_username,
                             ssh_host=host.host_ip,
                             remote_dest=dest + project.name)
            git.deploy(cmd)
deployService = DeployService()
