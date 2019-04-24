# -*- coding:utf-8 -*-
from localshell import LocalShell
from main import logger


class Git(object):

    def __init__(self, dest, url):
        self.dest = dest
        self.url = url
        self.location = "/home/itcast/Desktop/deployProjects/"

    def local_branch(self):
        shell = "cd {0} && git branch".format(self.location+self.dest)
        stdout = LocalShell.check_output(shell, shell=True)
        stdout = stdout.strip().split("\n")
        stdout = [s.strip("* ") for s in stdout]
        return stdout

    def remote_branch(self):
        shell = "cd {0} && git branch -r".format(self.location+self.dest)
        stdout = LocalShell.check_output(shell, shell=True)
        stdout = stdout.strip().split("\n")
        stdout = [s.strip(" ").split("/", 1)[1] for s in stdout if "->" not in
                  s]
        return stdout

    def log(self):
        shell = ("cd {0} && git log -20 --pretty=\"%h  %an  %s\""
                 ).format(self.location+self.dest)
        stdout = LocalShell.check_output(shell, shell=True)
        stdout = stdout.strip().split("\n")
        stdout = [s.split("  ", 2) for s in stdout]
        return [{"abbreviated_commit": s[0],
                 "author_name": s[1],
                 "subject": s[2]}
                for s in stdout]

    def clone(self):
        logger.debug("clone repo:")
        shell = ("mkdir -p {0} && cd {0} && git clone -q {1}"
                 ).format(self.location,self.url)
        rc = LocalShell.call(shell, shell=True)
        if rc == 128:
            shell = ("cd {0} && git pull").format(self.location+self.dest)
            rc = LocalShell.call(shell, shell=True)
            # branch name required
            if rc == 0:
                return
        if rc != 0:
            raise RuntimeError

    def checkout_branch(self, branch, version=""):
        logger.debug("checkout branch:")
        if branch in self.local_branch():
            LocalShell.check_call("cd {0} && git checkout -q {1} && git pull "
                                  "-q origin {1} && git reset --hard {2}"
                                  .format(self.location+self.dest, branch, version),
                                  shell=True)
        else:
            LocalShell.check_call("cd {0} && git checkout -q -b {1} -t "
                                  "origin/{1} && git pull -q origin {1} && "
                                  "git reset --hard {2}"
                                  .format(self.location+self.dest, branch, version),
                                  shell=True)

    def package(self,branch):
        logger.debug("package project:")
        shell = ("cd {0} && git checkout {1} && mvn package -DskipTests=true").format(self.location+self.dest, branch)
        rc = LocalShell.call(shell, shell=True)
        if rc != 0:
            raise RuntimeError

    def deploy(self,cmd):
        rc = LocalShell.call(cmd,shell=True)
        if rc != 0:
            raise RuntimeError
