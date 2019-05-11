# -*- coding:utf-8 -*-
from Base import Base
from main.model.Deploy import deploys
from main.service.ProjectService import projectService
from main.service.HostService import hostService
from main.service.ProjectHostService import projectHostService
from main.utils.git import Git
import threading

cond = threading.Condition()
firstDeploySuccess = False

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
        prohosts = projectHostService.find(project_id=form.project_id).all()
        t = threading.Thread(target=deploy_thread,args=(prohosts,git,project,), name="deploy-thread")
        t.start()
        t.join()

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

def deploy_thread(prohosts,git,project):
    dest = "/home/aaa/"
    if len(prohosts) == 1:
        print("只发布一台机器 :"+str(prohosts[0]))
        host = hostService.get(prohosts[0].host_id)
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
    else:
        print("发布更多机器 :" + str(prohosts))
        prohost = prohosts[0]
        print("发布第一台机器: "+str(prohost))

        cond.acquire()
        print("部署中第一台中 ....")
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
        print("部署中第一台成功")
        print("等待通知")
        global firstDeploySuccess
        firstDeploySuccess = True
        cond.wait()  # 线程挂起

        print("开始发布后续机器")

        for i in range(1,len(prohosts)):
            host = hostService.get(prohosts[i].host_id)
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
        cond.release()
def deploy_Notify():
    cond.acquire()

    print('继续发布')
    cond.notify()

    cond.release()

def flag():
    return firstDeploySuccess
