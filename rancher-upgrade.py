#!/usr/bin/python

import sys, os


class Main:

    def __init__(self, stack):
        self.stack = stack
        #VARIABLES DE ACCESO A RANCHER
        self.rancherUrl = 'http://localhost:8080'
        self.accessKey = '24870D10632AAB97C5A2'
        self.privateKey = 'fwenwL5ZA5q14zXrEAtHANVj43BdG6GdoSnBFrSc'
        self.composePath = '/home/jorge/Workspace/Rancher/compose/{0}/{1}-compose.yml'

        self.uuaa = stack.split("-")[0]
        self.cmd = 'rancher-compose -f ~/Workspace/Rancher/compose/{0}/{1}-docker-compose.yml -p {0} --access-key {2} --secret-key {3} --url {4}/v1/projects/1a7 -r ~/Workspace/Rancher/compose/{0}/{1}-rancher-compose.yml up -u -c -d'

    def upgrade(self):
        composePath = self.composePath.format(self.uuaa, self.stack)
        cmd = self.cmd.format(self.uuaa, self.stack, self.accessKey, self.privateKey, self.rancherUrl)

        self.launch(cmd)

    def launch(self, cmd):
        output = os.popen(cmd).read().strip()


if __name__ == "__main__":
    stack = sys.argv[1]
    order = sys.argv[2]

    main = Main(stack)
    if order == 'upgrade':
        main.upgrade()
